from flask_restful import Resource

class Download(Resource):

    def get(self):
        return {'download': 'success'}