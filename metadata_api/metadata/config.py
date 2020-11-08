class Config(object):
    DEBUG = False


class DevConfig(Config):
    name = 'DEVELOPMENT'
    DEBUG = True


class ProdConfig(Config):
    name = 'PRODUCTION'


configuration = {
    'DEV': DevConfig,
    'PROD': ProdConfig
}