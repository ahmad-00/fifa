import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = eval(os.environ.get('DEBUG'))
    DB_NAME = os.environ.get('POSTGRES_DB')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = int(os.environ.get('DB_PORT'))
    DB_USERNAME = os.environ.get('POSTGRES_USER')
    DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    LOG_LEVEL = os.environ.get('LOG_LEVEL')
