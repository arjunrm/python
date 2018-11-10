from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def check_posted_data(posted_data, func_name):
    if func_name == "add" or func_name == "subtract" or func_name == "multiply":
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        else:
            return 200
    elif func_name == "divide":
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        elif posted_data["y"] == 0:
            return 302
        else:
            return 200

@api.resource("/add")
class Add(Resource):
    # Add was requested using POST
    def post(self):
        # get posted data
        posted_data = request.get_json()

        # verify validity of posted data
        status_code = check_posted_data(posted_data, "add")

        if status_code != 200:
            ret_error = {
                "Message" : "Error occured",
                "Status Code" : status_code
            }
            return jsonify(ret_error)

        x = posted_data["x"]
        y = posted_data["y"]
        x = int(x)
        y = int(y)

        ret = x + y
        ret_map = {
            "Message" : ret,
            "Status Code" : 200
        }

        return jsonify(ret_map)

@api.resource("/subtract")
class Subtract(Resource):
    def post(self):
        # get posted data
        posted_data = request.get_json()

        # verify validity of posted data
        status_code = check_posted_data(posted_data, "subtract")

        if status_code != 200:
            ret_error = {
                "Message" : "Error occured",
                "Status Code" : status_code
            }
            return jsonify(ret_error)

        x = posted_data["x"]
        y = posted_data["y"]
        x = int(x)
        y = int(y)

        ret = x - y
        ret_map = {
            "Message" : ret,
            "Status Code" : 200
        }

        return jsonify(ret_map)

@api.resource("/multiply")
class Multiply(Resource):
    def post(self):
        # get posted data
        posted_data = request.get_json()

        # verify validity of posted data
        status_code = check_posted_data(posted_data, "multiply")

        if status_code != 200:
            ret_error = {
                "Message" : "Error occured",
                "Status Code" : status_code
            }
            return jsonify(ret_error)

        x = posted_data["x"]
        y = posted_data["y"]
        x = int(x)
        y = int(y)

        ret = x * y
        ret_map = {
            "Message" : ret,
            "Status Code" : 200
        }

        return jsonify(ret_map)

@api.resource("/divide")
class Divide(Resource):
    def post(self):
        # get posted data
        posted_data = request.get_json()

        # verify validity of posted data
        status_code = check_posted_data(posted_data, "divide")

        if status_code != 200:
            ret_error = {
                "Message" : "Error occured",
                "Status Code" : status_code
            }
            return jsonify(ret_error)

        x = posted_data["x"]
        y = posted_data["y"]
        x = float(x)
        y = float(y)

        ret = x / y
        ret_map = {
            "Message" : ret,
            "Status Code" : 200
        }

        return jsonify(ret_map)

# api.add_resource(Add, "/add")
# api.add_resource(Subtract, "/subtract")
# api.add_resource(Multiply, "/multiply")
# api.add_resource(Divide, "/divide")

if __name__ == "__main__":
    app.run(debug=True)
