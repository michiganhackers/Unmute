class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://unmute:unmute@localhost/unmute-db'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory'
