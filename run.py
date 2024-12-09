from flask import Flask, request, jsonify
from flask import Flask, render_template, send_from_directory
from database import *

app = Flask(__name__)

create_tables()

@app.route('/')
def index():
    return "Hello, welcome!"

@app.route('/add_user', methods=['POST'])
def add_user_route():
    name = request.json.get('name')
    email = request.json.get('email')
    response = add_user(name, email)
    return jsonify(response)

@app.route('/get_users', methods=['GET'])
def get_users_route():
    users = get_users()
    return jsonify([{"id": user[0], "name": user[1], "email": user[2], "created_at": user[3]} for user in users])

@app.route('/delete_user', methods=['DELETE'])
def delete_user_route():
    user_id = request.json.get('user_id')
    response = delete_user(user_id)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
