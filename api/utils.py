from api.sqlalchemy import engine, Base
from api.models import Contact


def create_tables():
    Base.metadata.create_all(bind=engine)


create_tables()
