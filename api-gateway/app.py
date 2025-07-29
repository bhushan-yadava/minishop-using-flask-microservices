from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return requests.get('http://user-service:5000/users').text
    return requests.post('http://user-service:5000/users', json=request.get_json()).text

@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return requests.get('http://product-service:5000/products').text
    return requests.post('http://product-service:5000/products', json=request.get_json()).text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
