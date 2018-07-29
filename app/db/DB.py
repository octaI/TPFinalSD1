from sqlalchemy.orm import sessionmaker

from app import config
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

Engine = create_engine("{}://{}@{}:{}/{}?{}".format(
    config.DB.DRIVER,
    config.DB.USER,
    config.DB.HOST,
    config.DB.PORT,
    config.DB.DATABASE.lower(),
    "&".join(["{}={}".format(key, value) for key, value in config.DB.SETTINGS.items()])
), pool_size=300)

Session = sessionmaker(bind=Engine)


def get_session():
    return Session()
