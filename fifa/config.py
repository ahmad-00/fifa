import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = eval(os.environ.get('DEBUG'))
    DB_NAME = os.environ.get('DB_NAME')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = int(os.environ.get('DB_PORT'))
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    LOG_LEVEL = os.environ.get('LOG_LEVEL')
