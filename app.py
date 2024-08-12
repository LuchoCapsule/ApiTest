from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/api/echo/<int:id>', methods=['GET'])
def echo_id(id):
    return jsonify(id=id)

@app.route('/api/todos', methods=['GET'])
def get_todos():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = response.json()
    return jsonify(todos)

if __name__ == "__main__":
    app.run(debug=True)