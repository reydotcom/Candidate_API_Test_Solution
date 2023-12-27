from flask import Flask, jsonify

from datetime import datetime
import pytz
import json
import random

from database import armenian_dishes, armenian_cities, ararat_info

app = Flask(__name__)


@app.route('/time', methods=['GET'])
def get_time():
    response = {
        "location": "Yerevan",
        "current_time": datetime.now(pytz.timezone('Europe/Yerevan')).strftime("%Y-%m-%d %H:%M:%S")
    }

    return jsonify(response), 200


@app.route('/armenian-cities', methods=['GET', 'POST'])
def get_cities():
    return jsonify(armenian_cities())


@app.route('/ararat-info', methods=['GET', 'POST'])
def get_ararat_info():
    return jsonify(ararat_info())


@app.route('/armenian-dishes', methods=['GET', 'POST'])
def get_dishes():
    return jsonify(armenian_dishes())


@app.route('/random-armenian-word', methods=['GET', 'POST'])
def get_random_word():

    with open('dictionary.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        index = random.randint(1, 98)
        value = data.get(str(index))
    return jsonify({'word': value})


if __name__ == "__main__":
    app.run(debug=True)
