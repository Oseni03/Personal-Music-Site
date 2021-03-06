import os
import string
import random


letters = string.ascii_letters


class BaseConfig(object):
    """base config"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("secret_key", ''.join(
        [random.choice(string.ascii_letters + string.digits) for n in range(16)]))
    UPLOAD_FOLDER = os.path.realpath('.') + '/app/static'


class TestingConfig(BaseConfig):
    """testing config"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ''
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    """dev config"""
    DEBUG = True 
    SQLALCHEMY_DATABASE_URI= "sqlite:///music.db"
    SECRET_KEY = '9ab803b32301726f09247060e35175'


class ProductionConfig(BaseConfig):
    """production config"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("")
