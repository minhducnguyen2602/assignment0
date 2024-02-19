from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from setting_database.conf.settings.base import DATABASE

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

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

