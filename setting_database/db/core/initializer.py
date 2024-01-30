from sqlalchemy import create_engine
from setting_database.conf.settings.base import DATABASE

# create database engine
engine = create_engine(
    "postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}".format(
        db_username=DATABASE['USERNAME'], 
        db_password=DATABASE['PASSWORD'],
        db_host=DATABASE['HOST'],
        db_port=DATABASE['PORT'],
        db_name=DATABASE['NAME']
    ),
    echo=True
)

# create a connection with the database
def create_connection():
    return engine.connect()