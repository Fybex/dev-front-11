from functools import reduce

from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route('/')
def index() -> str:
    with open('contents.html') as contents:
        return contents.read()


def request_handler(func: callable) -> callable:
    def wrapper():
        data = request.get_json()
        total = func(data.values())
        return jsonify(
            total=total,
        )
    return wrapper


@app.route('/add', methods=['POST'], endpoint='add')
@request_handler
def add(data: list[int]) -> int:
    return sum(data)


@app.route('/multiply', methods=['POST'], endpoint='multiply')
@request_handler
def multiply(data: list[int]) -> int:
    return reduce(lambda x, y: x * y, data)


@app.route('/minmax', methods=['POST'], endpoint='minmax')
@request_handler
def minmax(data: list[int]) -> dict[str, int]:
    return {
        'min': min(data),
        'max': max(data),
    }



