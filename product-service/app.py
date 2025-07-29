from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(
        host=os.environ.get('PG_HOST', 'localhost'),
        database='minishop',
        user='postgres',
        password='password'
    )

@app.route('/products', methods=['GET'])
def get_products():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT name FROM products')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([r[0] for r in rows])

@app.route('/products', methods=['POST'])
def create_product():
    conn = get_conn()
    cur = conn.cursor()
    data = request.get_json()
    cur.execute('INSERT INTO products (name) VALUES (%s)', (data['name'],))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Product added'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
