import json
import random

from flask import Flask, jsonify, request

from datetime import datetime
import pytz

from db.orm import SyncORM


app = Flask(__name__)


@app.route('/time', methods=['GET'])
def get_time():
    user_time = request.args.get('user_time')
    user_time = datetime.strptime(user_time, '%Y-%m-%d %H:%M:%S')

    armenian_time = datetime.now(pytz.timezone('Asia/Yerevan')).strftime('%Y-%m-%d %H:%M:%S')
    armenia_time = datetime.strptime(armenian_time, '%Y-%m-%d %H:%M:%S')

    if user_time > armenia_time:
        return jsonify({"difference": str(user_time - armenia_time)}), 200
    return jsonify({"difference": f'-{armenia_time - user_time}'}), 200


@app.route('/armenian-cities', methods=['GET'])
def get_cities():
    return jsonify(SyncORM.select_armenian_cities()), 200


@app.route('/ararat-info', methods=['GET'])
def get_ararat_info():
    return jsonify(SyncORM.select_ararat_info()), 200


@app.route('/armenian-dishes', methods=['GET'])
def get_dishes():
    return jsonify(SyncORM.select_armenian_dishes()), 200


@app.route('/random-armenian-word', methods=['GET'])
def get_random_word():

    with open('../dictionary.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        index = random.randint(0, 98)
        value = data.get(str(index))
    return jsonify({'word': value}), 200


def main():
    SyncORM.create_tables()
    app.run(debug=True)


if __name__ == "__main__":
    main()
