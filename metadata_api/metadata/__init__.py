from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from metadata.config import configuration
import os

app = Flask(__name__)
env_config = configuration[os.getenv('ENV', 'PROD')]
app.config.from_object(env_config)
api = Api(app)
mongo = PyMongo(app)


def create_app():

    #db.create_all()

    from endpoints.upload import Upload
    from endpoints.download import Download

    api.add_resource(Upload, '/upload')
    api.add_resource(Download, '/download')

    return app

