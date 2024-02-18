import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from config import settings


sync_engine = create_engine(url=settings.DATABASE_URL_psycopg(), echo=True)
sync_session_factory = sessionmaker(sync_engine)


class Base(DeclarativeBase):
    pass


def data_from_json():
    with open('../data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
