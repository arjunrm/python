"""
Resources       Address             Protocol    Params                          Return Codes
Add             /add                POST        username, pwd                   200 OK, 301 Invalid Username
Transfer        /transfer           POST        username, pwd, to_acc, amt      200 OK, 301 Invalid Username, 302 Invalid Password, 303 Insufficient Balance, 304 Invalid Amount
CheckBalance    /balance            POST        username, pwd                   200 OK, 301 Invalid Username, 302 Invalid Password
TakeLoan        /takeloan           POST        username, pwd, amt              200 OK, 301 Invalid Username, 302 Invalid Password, 304 Invalid Amount
PayLoan         /payloan            POST        username, pwd, amt              200 OK, 301 Invalid Username, 302 Invalid Password, 303 Insufficient Balance, 304 Invalid Amount
"""

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
from bson.json_util import dumps
import bcrypt

app = Flask(__name__)
api = Api(app=app)

client = MongoClient("mongodb://db:27017")
db = client.BankApi
users = db["Users"]
# bank = users.insert_one({
#     "username" : "BANK",
#     "own" : 0,
#     "debt" : 0
#     })

def user_exists(username):
    if users.find({"username":username}).count() == 0:
        return False
    else:
        return True

def verify_pwd(username, password):
    # get hash_pwd stored in db
    hash_pwd = users.find({"username" : username})[0]["password"]

    if bcrypt.hashpw(password.encode('utf8'), hash_pwd) == hash_pwd:
        return True
    else:
        return False

def cash_with_user(username):
    cash = users.find({"username" : username})[0]["own"]
    return cash

def debt_with_user(username):
    debt = users.find({"username" : username})[0]["debt"]
    return debt

def update_balance(username, balance):
    users.update({
            "username" : username
        },
        {
            "$set" : {
                "own" : balance
            }
        })

def update_debt(username, debt):
    users.update({
            "username" : username
        },
        {
            "$set" : {
                "debt" : debt
            }
        })

def ret_json(status, message):
    retJson = {
        "status" : status,
        "message" : message
    }
    return jsonify(retJson)

@api.resource("/dispusers")
class DispUsers(Resource):
    def get(self):
        return dumps(users.find())

@api.resource("/dropusers")
class DropUsers(Resource):
    def get(self):
        result = users.delete_many({})
        retJson = {
            "status" : 200,
            "message" : "Dropped documents in users collection",
            "deleted count" : result.deleted_count()
        }
        return jsonify(retJson)

@api.resource("/register")
class Register(Resource):
    def post(self):
        # get the posted data
        posted_data = request.get_json()

        # get the data
        username = posted_data["username"]
        password = posted_data["password"]

        # check if user exists
        if user_exists(username):
            return ret_json(301, "Invalid username")

        # hash(password + salt)
        hash_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        # store in db
        users.insert_one({
            "username" : username, 
            "password" : hash_password,
            "own" : 0,
            "debt" : 0
            })

        # create return json message
        return ret_json(200, "You have successfully signed up to the API")

@api.resource("/add")
class Add(Resource):
    def post(self):
        # get the posted data
        posted_data = request.get_json()

        # get the data
        username = posted_data["username"]
        password = posted_data["password"]
        amount = posted_data["amount"]

        # check if user exists
        if not user_exists(username):
            return ret_json(301, "Invalid username")

        if not verify_pwd(username, password):
            return ret_json(302, "Invalid password")

        if amount <= 0:
            return ret_json(304, "Invalid Amount")

        cash = cash_with_user(username)
        amount -= 1  # reduce amount by 1 as transaction fee to the BANK
        bank_cash = cash_with_user("BANK")
        update_balance("BANK", bank_cash + 1)
        update_balance(username, cash + amount)

        return ret_json(200, f"Successfully added {amount} into your account")

@api.resource("/transfer")
class Transfer(Resource):
    def post(self):
        # get the posted data
        posted_data = request.get_json()

        # get the data
        username = posted_data["username"]
        password = posted_data["password"]
        rec_username = posted_data["rec_username"]
        amount = posted_data["amount"]

        # check if user exists
        if not user_exists(username):
            return ret_json(301, "Invalid username")

        if not verify_pwd(username, password):
            return ret_json(302, "Invalid password")

        if amount <= 0:
            ret_json(304, "Invalid Amount")

        cash = cash_with_user(username)
        if cash <= 0:
            return ret_json(303, "Insufficient Balance")

        if not user_exists(rec_username):
            return ret_json(301, "Receiver username doesn't exist")
        
        cash_from = cash_with_user(username)
        cash_to = cash_with_user(rec_username)
        bank_cash = cash_with_user("BANK")

        cash_from -= 1
        cash_to -= 1
        update_balance("BANK", bank_cash + 2)

        update_balance(username, cash_from - amount)
        update_balance(rec_username, cash_to + amount)

        return ret_json(200, f"Transfered '{amount}' from '{username}' to '{rec_username}' successfully")

@api.resource("/balance")
class Balance(Resource):
    def post(self):
        # get the posted data
        posted_data = request.get_json()

        # get the data
        username = posted_data["username"]
        password = posted_data["password"]

        # check if user exists
        if not user_exists(username):
            return ret_json(301, "Invalid username")

        if not verify_pwd(username, password):
            return ret_json(302, "Invalid password")

        retJson = users.find({
            "username" : username
        } , {
            "password" : 0, # 0 is to avoid getting these fields
            "_id" : 0
        })[0]
        return retJson

@api.resource("/takeloan")
class TakeLoan(Resource):
    def post(self):
        # get the posted data
        posted_data = request.get_json()

        # get the data
        username = posted_data["username"]
        password = posted_data["password"]
        amount = posted_data["amount"]

        # check if user exists
        if not user_exists(username):
            return ret_json(301, "Invalid username")

        if not verify_pwd(username, password):
            return ret_json(302, "Invalid password")

        cash = cash_with_user(username)
        debt = debt_with_user(username)
        update_balance(username, cash + amount)
        update_debt(username, debt + amount)

        return ret_json(200, f"Successfully added '{amount}' loan amount to your account")

@api.resource("/payloan")
class PayLoan(Resource):
    def post(self):
        # get the posted data
        posted_data = request.get_json()

        # get the data
        username = posted_data["username"]
        password = posted_data["password"]
        amount = posted_data["amount"]

        # check if user exists
        if not user_exists(username):
            return ret_json(301, "Invalid username")

        if not verify_pwd(username, password):
            return ret_json(302, "Invalid password")

        if amount <= 0:
            return ret_json(304, "Invalid Amount")

        cash = cash_with_user(username)
        if cash < amount:
            return ret_json(303, "Insufficient Balance")

        debt = debt_with_user(username)
        update_balance(username, cash - amount)
        update_debt(username, debt - amount)

        return ret_json(200, f"Successfully paid '{amount}' your loan")

if __name__ == "__main__":
    app.run("0.0.0.0")

