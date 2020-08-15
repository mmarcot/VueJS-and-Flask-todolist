from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app)

items = [
    {'id': 0, 'text': "Faire le ménage"},
    {'id': 1, 'text': "Préparer le repas"},
    {'id': 2, 'text': "Faire le repassage"},
    {'id': 3, 'text': "Go dodo"},
]

@app.route('/')
def index():
    return '<h1>TODO list API</h1>'

@app.route('/items')
def get_items():
    return jsonify(items)


app.run()