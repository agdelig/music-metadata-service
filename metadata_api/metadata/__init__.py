from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from endpoints.upload import Upload
from endpoints.download import Download
from metadata.config import configuration
import os


def create_app():
    app = Flask(__name__)
    env_config = configuration[os.getenv('ENV', 'PROD')]
    app.config.from_object(env_config)

    api = Api(app)

    #db = SQLAlchemy(app)
    #db.create_all()

    api.add_resource(Upload, '/upload')
    api.add_resource(Download, '/download')

    return app

