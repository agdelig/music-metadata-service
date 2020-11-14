class Config(object):
    DEBUG = False


class DevConfig(Config):
    name = 'DEVELOPMENT'
    DEBUG = True
    MONGO_DBNAME = 'music-meta'
    MONGO_URI = 'mongodb://localhost:27017/music-meta'


class ProdConfig(Config):
    name = 'PRODUCTION'
    MONGO_DBNAME = 'music-meta'
    MONGO_URI = 'mongodb://mongo-meta-db:27017/music-meta'



configuration = {
    'DEV': DevConfig,
    'PROD': ProdConfig
}