"""
Registration of a user
Each user gets 10 tokens
Store a sentence on our db for 1 token
Retreive his stored sentence from our db for 1 token
"""

"""
REST API chart
Resource            Address         Protocol        Param                   Response + Status code
------------------------------------------------------------------------------------------------------------------------------
Register            /register       POST            username, pwd           200 OK
Store sentence      /store          POST            username, pwd, sentence 200 OK, 301 Out of tokens, 302 Invalid credentials
Retreive sentence   /getsentence    POST            username, pwd           200 OK, 301 Out of tokens, 302 Invalid credentials
Get no of tokens    /gettokens      POST            username, pwd           200 OK, 302 Invalid credentials
"""

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
api = Api(app=app)

client = MongoClient("mongodb://db:27017")
db = client.SentencesDB # db
users = db["Users"] # collections

def verify_pwd(username, password):
    # get hashed pwd stored in db
    hash_pwd = users.find({
        "username" : username
    })[0]["password"]
    if bcrypt.hashpw(password.encode('utf8'), hash_pwd) == hash_pwd:
        return True
    else:
        return False

def get_tokens(username):
    tokens = users.find({
        "username" : username
        })[0]["tokens"]
    return tokens

@api.resource("/register")
class Register(Resource):
    def post(self):
        # get the posted data
        posted_data = request.get_json()

        # get the data
        username = posted_data["username"]
        password = posted_data["password"]

        # hash(password + salt)
        hash_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        # store in db
        users.insert_one({
            "username" : username, 
            "password" : hash_password,
            "sentence" : "",
            "tokens" : 6
            })

        # create return json message
        retJson = {
            "status" : 200,
            "message" : "You have successfully signed up"
        }

        return jsonify(retJson)

@api.resource("/store")
class Store(Resource):
    def post(self):
        # get the posted data
        posted_data = request.get_json()

        # get the data
        username = posted_data["username"]
        password = posted_data["password"]
        sentence = posted_data["sentence"]

        # verify credentials
        correct_pwd = verify_pwd(username, password)
        if not correct_pwd:
            retJson = {
                "status" : 302,
                "message" : "Invalid credentials"
            }
            return jsonify(retJson)

        # verify user has enough tokens
        tokens = get_tokens(username)
        if tokens <= 0:
            retJson = {
                "status" : 301,
                "message" : "Not enough tokens"
            }
            return jsonify(retJson)

        # store the sentence
        users.update_one({
                "username" : username
            },
            {
                "$set" : {
                    "sentence" : sentence,
                    "tokens" : tokens - 1
                }
            })

        retJson = {
            "status" : 200,
            "message" : "Successfully stored a sentence"
        }
        return jsonify(retJson)

@api.resource("/getsentence")
class GetSentence(Resource):
    def post(self):
        # get the posted data
        posted_data = request.get_json()

        # get the data
        username = posted_data["username"]
        password = posted_data["password"]

        # verify credentials
        correct_pwd = verify_pwd(username, password)
        if not correct_pwd:
            retJson = {
                "status" : 302,
                "message" : "Invalid credentials"
            }
            return jsonify(retJson)

        # verify user has enough tokens
        tokens = get_tokens(username)
        if tokens <= 0:
            retJson = {
                "status" : 301,
                "message" : "Not enough tokens"
            }
            return jsonify(retJson)

        sentence = users.find({
            "username" : username
        })[0]["sentence"]

        # reduce 1 token
        users.update_one({
            "username" : username
        },
        {
            "$set" : {
                "tokens" : tokens - 1
            }
        })

        retJson = {
            "status" : 200,
            "message" : sentence
        }
        return jsonify(retJson)

@api.resource("/gettokens")
class GetTokens(Resource):
    def post(self):
        # get the posted data
        posted_data = request.get_json()

        # get the data
        username = posted_data["username"]
        password = posted_data["password"]

        # verify credentials
        correct_pwd = verify_pwd(username, password)
        if not correct_pwd:
            retJson = {
                "status" : 302,
                "message" : "Invalid credentials"
            }
            return jsonify(retJson)

        tokens = users.find({
            "username" : username
        })[0]["tokens"]

        retJson = {
            "status" : 200,
            "message" : tokens
        }
        return jsonify(retJson)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
