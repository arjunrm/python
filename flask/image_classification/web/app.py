"""
Resources       Address     Protocol    Params                              Return codes
Register        /register   POST        username, pwd                       200 OK, 301 Invalid username
Classify        /classify   POST        username, pwd, url/*.jpeg           200 OK, 301 Invalid username, 302 Invalid pwd, 303 Out of tokens
Refill          /refill     POST        username, pwd, admin_pwd, refill    200 OK, 301 Invalid username, 302 Invalid pwd, 304 Invalid admin credentials
"""

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
from bson.json_util import dumps
import bcrypt
import requests
import subprocess
import json

app = Flask(__name__)
api = Api(app=app)

client = MongoClient("mongodb://db:27017")
db = client.ImageRecognition
users = db["users"]
admin = db["admin"]

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

@api.resource("/dispadmin")
class DispAdmin(Resource):
    def get(self):
        return dumps(admin.find())

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
            "tokens" : 2
            })

        # create return json message
        return ret_json(200, "You have successfully signed up to the API")

@api.resource("/classify")
class Classify(Resource):
    def post(self):
        # get the posted data
        posted_data = request.get_json()

        # get the data
        username = posted_data["username"]
        password = posted_data["password"]
        url = posted_data["url"]

        # check if user exists
        if not user_exists(username):
            return ret_json(301, "Invalid username")

        if not verify_pwd(username, password):
            return ret_json(302, "Invalid password")

        tokens = get_tokens(username)
        if tokens <= 0:
            return ret_json(303, "Out of tokens")

        r = requests.get(url)
        retJson = {}
        with open("temp.jpg", "wb") as f:
            f.write(r.content)
            proc = subprocess.Popen('python classify_image.py --model_dir=. --image_file=temp.jpg', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            proc.communicate()[0]
            proc.wait()
            with open("text.txt") as g:
                retJson = json.load(g)

        users.update({
            "username" : username,
        },
        {
            "$set" : {
                "tokens" : tokens - 1
            }
        })

        return retJson

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
    app.run(host="0.0.0.0", debug=True)
