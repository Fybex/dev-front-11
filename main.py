from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route('/')
def index() -> str:
    with open('contents.html') as contents:
        return contents.read()


@app.route('/add', methods=['POST'])
def add() -> Response:
    data = request.get_json()
    total = data['a'] + data['b']
    return jsonify(
        total=total,
    )


@app.route('/multiply', methods=['POST'])
def multiply() -> Response:
    data = request.get_json()
    total = data['a'] * data['b']
    return jsonify(
        total=total,
    )
