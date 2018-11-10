from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome to Hello World!"

@app.route('/details')
def details():
    age = 30 + 4
    ret_json = {
        'Name' : 'Arjun',
        'Age' : age,
        'Place' : 'Bangalore',
        'Array' : [1,2,3,4,"abc"],
        'Array of JSON objects' : [
            {
                'Field1' : 1
            },
            {
                'Field2' : 2
            }
        ],
        'Array of nested arrays' : [
            {
                'Nested array' : [
                    {
                        'Field1' : 1,
                        'Name' : 'James'
                    },
                    {
                        'Field2' : 2,
                        'Name' : 'Bond'
                    }
                ]
            }
        ]
    }

    return jsonify(ret_json)

if __name__ == "__main__":
    app.run(debug=True)
