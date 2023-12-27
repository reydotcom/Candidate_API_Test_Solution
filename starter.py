from sqlalchemy import create_engine, text
import logging
import json

from App.config import settings

engine = create_engine(url=settings.DATABASE_URL_psycopg())

logging.basicConfig(level=logging.DEBUG)


def data_from_json(name):
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data.get(name)


def add_ararat_info():
    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE ararat_info (text TEXT);"))
        logging.info('<--The table ararat_info has been created-->')

        data = data_from_json('ararat_info')
        logging.info('<--The data has been successfully retrieved from the JSON file-->')

        req = text("INSERT INTO ararat_info (text) VALUES (:value)")
        conn.execute(req, {"value": (data, )})
        logging.info('<--The data has been successfully added to the table.-->')

        conn.commit()


def add_cities():
    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE cities (name VARCHAR, population BIGINT);"))
        logging.info('<--The table cities has been created-->')

        data = data_from_json('cities_dict')
        logging.info('<--The data has been successfully retrieved from the JSON file-->')

        for key, value in data.items():
            req = text("INSERT INTO cities (name, population) VALUES (:value1, :value2)")
            params = {"value1": key, "value2": int(value)}
            conn.execute(req, params)

        logging.info('<--The data has been successfully added to the table.-->')
        conn.commit()


def add_dishes():
    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE dishes (name VARCHAR);"))
        logging.info('<--The table dishes has been created-->')

        data = data_from_json('dishes_dict')
        logging.info('<--The data has been successfully retrieved from the JSON file-->')

        for value in data.values():
            req = text("INSERT INTO dishes (name) VALUES (:value1)")
            conn.execute(req, {"value1": value})

        logging.info('<--The data has been successfully added to the table.-->')
        conn.commit()


logging.info('<--Running the function "add_ararat_info"-->')
add_ararat_info()

logging.info('<--Running the function "add_cities"-->')
add_cities()

logging.info('<--Running the function "add_dishes"-->')
add_dishes()
