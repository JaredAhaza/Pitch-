import os

class Config:
    '''
    The general parent configurations
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SIMPLEMDE_JS_IIFE = True
    SIMPLE_USE_CDN = True
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jared:postgres@localhost/pitchup'

    @staticmethod
    def init_app(app):
        app

class ProdConfig(Config):
    '''
    Child configurations with config passed in as a class
    ''' 
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    '''
    Child configyrations with config passed in as a class to test database relationship
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jared:postgres@localhost/pitchup'


class DevConfig(Config):
    '''
    Chuld configurations with config passed in as a class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jared:postgres@localhost/pitchup'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}