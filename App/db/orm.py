from sqlalchemy import select, insert

from db.database import sync_engine, sync_session_factory, Base, data_from_json
from db.models import AraratInfo, Cities, Dishes


class SyncORM:
    @staticmethod
    def create_tables():
        Base.metadata.create_all(sync_engine)

        with sync_session_factory() as session:
            data = data_from_json()

            ararat_info = [{'text': data.get('ararat_info')}]
            cities = [{'name': key, 'population': value} for key, value in data.get('cities_dict').items()]
            dishes = [{'name': item} for item in data.get('dishes_dict').values()]

            session.execute(insert(AraratInfo).values(ararat_info))
            session.execute(insert(Cities).values(cities))
            session.execute(insert(Dishes).values(dishes))

            session.commit()

    @staticmethod
    def select_armenian_cities():
        with sync_session_factory() as session:
            result = session.execute(select(Cities))

            cities = [{'name': item.name, 'population': item.population} for item in result.scalars().all()]

            return {'cities': cities}

    @staticmethod
    def select_ararat_info():
        with sync_session_factory() as session:
            result = session.execute(select(AraratInfo.text))
            return {'text': result.scalars().all()}

    @staticmethod
    def select_armenian_dishes():
        with sync_session_factory() as session:
            result = session.execute(select(Dishes.name))
            data = [item for item in result.scalars().all()]

            return {'dishes': data}
