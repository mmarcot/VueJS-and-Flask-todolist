from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3


app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_items_dict():
    conn = get_db_connection()
    res = conn.execute("SELECT * from todoitems").fetchall()
    conn.close()
    return [dict(item) for item in res]

@app.route('/')
def index():
    return '<h1>TODO list API</h1>'

@app.route('/items')
def get_items():
    return jsonify(get_items_dict())

@app.route('/additem', methods=('GET', 'POST'))
def add_item():
    if request.method == 'POST':
        data = request.get_json()
        conn = get_db_connection()
        conn.execute("insert into todoitems (content) values (?)", (data['content'],))
        conn.commit();
        conn.close();
        return jsonify({'status': 'success', 'message': 'item added'})

    return jsonify(get_items_dict())

app.run()