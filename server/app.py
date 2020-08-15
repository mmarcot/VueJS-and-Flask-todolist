from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3


app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app)

ITEMS = [
    {'id': 0, 'text': "Faire le ménage"},
    {'id': 1, 'text': "Préparer le repas"},
    {'id': 2, 'text': "Faire le repassage"},
    {'id': 3, 'text': "Go dodo"},
]

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return '<h1>TODO list API</h1>'

@app.route('/items')
def get_items():
    conn = get_db_connection()
    res = conn.execute("SELECT * from todoitems").fetchall()
    conn.close()
    return jsonify([dict(item) for item in res])

@app.route('/additem', methods=('GET', 'POST'))
def add_item():
    if request.method == 'POST':
        data = request.get_json()
        ITEMS.append({

        })


app.run()