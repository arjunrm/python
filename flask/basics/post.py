import flask
from flask import Flask, jsonify, Request

app = Flask(__name__)

@app.route('/')
def main_page():
    return "Welcome to main page"

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
    # get x and y from posted data
    data_dict = flask.request.get_json()

    if "y" not in data_dict:
        return "ERROR", 400

    x = data_dict["x"]
    y = data_dict["y"]

    z = x + y

    res_dict = {
        "result" : z
        }

    return jsonify(res_dict)

@app.route('/json_obj')
def json_obj():
    data_dict = {
        "Name" : "James",
        "Age" : 42
    }
    return jsonify(data_dict)

if __name__ == "__main__":
    app.run(debug=True)
