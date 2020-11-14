from flask_restful import Resource, reqparse
from common import _query_db_concate, _query_to_base64_csv

class Download(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('iswc',
                            type=list,
                            help='List of iswc',
                            required=True,
                            location='json')
        self.req_parses = parser

    def post(self):
        iswcs = self.req_parses.parse_args(strict=True).get('iswc', None)
        file = _query_to_base64_csv(iswcs)

        return{
            'file': file,
            'responce': {
                'code': '200',
                'status': 'success'
            }
        }
