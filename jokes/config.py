import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Config:
    SECRET_KEY='fa9e3c004f5e6d8d1abd02fc'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SLQLALCHEMY_ECHO=True


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///'+BASE_DIR +'\jokes.db'
    DEBUG=True

class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI')


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///'+BASE_DIR+'\jokes.db'


