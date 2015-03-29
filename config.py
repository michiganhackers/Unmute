class Config(object):
    DEBUG = False
    DATABASE_URI = 'sqlite:///dev.db'

class ProductionConfig(Config):
    DATABASE_URI = 'postgresql+psycopg2://@localhost/db'

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite://:memory'
