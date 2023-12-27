from sqlalchemy import URL, create_engine, text
from config import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg(),
    pool_size=5,
    max_overflow=10,
)


def armenian_cities():
    with engine.connect() as conn:
        res = conn.execute(text("SELECT * FROM cities"))
        cities = []
        for item in res.fetchall():
            cities_list = {'name': item[0], 'population': item[1]}
            cities.append(cities_list)

        return {'cities': cities}


def ararat_info():
    with engine.connect() as conn:
        res = conn.execute(text("SELECT text FROM ararat_info"))
        return {'text': res.fetchall()[0][0]}


def armenian_dishes():
    with engine.connect() as conn:
        res = conn.execute(text("SELECT * FROM dishes"))
        data = [i[0] for i in res.fetchall()]

        return {'dishes': data}
