
from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)
client = MongoClient(os.environ.get('MONGO_URI', 'mongodb://localhost:27017/'))
db = client['minishop']
users = db['users']

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.find({}, {'_id': 0})))

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    users.insert_one(data)
    return jsonify({'message': 'User created'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
