from flask import Flask, jsonify, request

from datetime import datetime
import pytz
import json
import random

from database import armenian_dishes, armenian_cities, ararat_info


app = Flask(__name__)


@app.route('/time', methods=['GET'])
def get_time():
    user_time = request.args.get('user_time')
    user_time = datetime.strptime(user_time, '%Y-%m-%d %H:%M:%S')

    armenian_time = datetime.now(pytz.timezone('Asia/Yerevan')).strftime('%Y-%m-%d %H:%M:%S')
    armenia_time = datetime.strptime(armenian_time, '%Y-%m-%d %H:%M:%S')

    if user_time > armenia_time:
        return jsonify({"difference": str(user_time - armenia_time)})
    return jsonify({"difference": f'-{armenia_time - user_time}'})


@app.route('/armenian-cities', methods=['POST'])
def get_cities():
    return jsonify(armenian_cities())


@app.route('/ararat-info', methods=['POST'])
def get_ararat_info():
    return jsonify(ararat_info())


@app.route('/armenian-dishes', methods=['POST'])
def get_dishes():
    return jsonify(armenian_dishes())


@app.route('/random-armenian-word', methods=['POST'])
def get_random_word():

    with open('../dictionary.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        index = random.randint(1, 98)
        value = data.get(str(index))
    return jsonify({'word': value})


if __name__ == "__main__":
    app.run(debug=True)
