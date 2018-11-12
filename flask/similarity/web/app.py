"""
Resources           Address         Protocol    Params                                                  Response + status code
Register            /register       POST        username, pwd                                           200 OK, 301 Invalid username
Detect similarity   /detect         POST        username, pwd, text1, text2                             200 OK, 301 Invalid username, 302 Invalid pwd, 303 Out of tokens
Refill tokens       /refill         POST        username, pwd, admin_username, admin_pwd, refill amount 200 OK, 301 Invalid username, 302 Invalid pwd, 304 Invalid admin credentials
"""

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
from bson.json_util import dumps
import bcrypt
import spacy

app = Flask(__name__)
api = Api(app=app)

client = MongoClient("mongodb://db:27017")
db = client.similarity # create similarity db
users = db["users"] # create users collection
admin = db["admin"] # create admin collection
admin.delete_many({})
# insert admin credentials into admin collection
admin.insert_one({
    "username" : "admin",
    "password" : bcrypt.hashpw("abc123".encode('utf8'), bcrypt.gensalt())
})

def user_exists(username):
    if users.count_documents({"username" : username}) == 0:
        return False
    else:
        return True

def verify_pwd(username, password):
    # get hashed pwd stored in db
    hash_pwd = users.find({
        "username" : username
    })[0]["password"]

    if bcrypt.hashpw(password.encode('utf8'), hash_pwd) == hash_pwd:
        return True
    else:
        return False

def verify_admin_credentials(username, password):
    if admin.count_documents({"username" : username}) == 1:
        hash_pwd = admin.find_one({"username" :username})["password"]
        if bcrypt.hashpw(password.encode('utf8'), hash_pwd) == hash_pwd:
            return True
        else:
            return False
    else:
        return False

def get_tokens(username):
    tokens = users.find_one({
        "username" : username
        })["tokens"]
    return tokens

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

@api.resource("/dispadmin")
class DispAdmin(Resource):
    def get(self):
        return dumps(admin.find())

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
            "tokens" : 2
            })

        # create return json message
        return ret_json(200, "You have successfully signed up to the API")

@api.resource("/detect")
class Detect(Resource):
    def post(self):
        # get the posted data
        posted_data = request.get_json()

        # get the data
        username = posted_data["username"]
        password = posted_data["password"]
        text1 = posted_data["text1"]
        text2 = posted_data["text2"]

        # check if user exists
        if not user_exists(username):
            return ret_json(301, "Invalid username")

        if not verify_pwd(username, password):
            return ret_json(302, "Invalid password")
        
        tokens = get_tokens(username)
        if tokens <= 0:
            return ret_json(303, "Out of tokens")

        # load nlp model
        import en_core_web_sm
        nlp = en_core_web_sm.load()

        text1 = nlp(text1)
        text2 = nlp(text2)

        # ratio is between 0 to 1, closer to 1, the more similar the text1/2 are
        ratio = text1.similarity(text2)

        retJson = {
            "status" : 200,
            "similarity" : ratio,
            "message" : "Similarity score calculated"
        }

        users.update_one({
            "username" : username
        },
        {
            "$set" : {
                "tokens" : tokens - 1
            }
        })

        return jsonify(retJson)

@api.resource("/refill")
class Refill(Resource):
    def post(self):
        # get the posted data
        posted_data = request.get_json()

        # get the data
        username = posted_data["username"]
        password = posted_data["password"]
        admin_username = posted_data["admin_username"]
        admin_password = posted_data["admin_password"]
        refill = posted_data["refill"]

        # check if user exists
        if not user_exists(username):
            return ret_json(301, "Invalid username")

        if not verify_pwd(username, password):
            return ret_json(302, "Invalid password")

        # verify admin credentials
        if not verify_admin_credentials(admin_username, admin_password):
            return ret_json(304, "Invalid admin credentials")

        tokens = get_tokens(username)
        users.update_one({
            "username" : username
        },
        {
            "$set" : {
                "tokens" : tokens + refill
            }
        })

        return ret_json(200, "Refilled successfully")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
