from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from endpoints.upload import Upload
from endpoints.download import Download
from metadata.config import configuration
import os

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy()


def create_app():
    env_config = configuration[os.getenv('ENV', 'PROD')]
    app.config.from_object(env_config)

    #db.create_all()

    api.add_resource(Upload, '/upload')
    api.add_resource(Download, '/download')

    return app

