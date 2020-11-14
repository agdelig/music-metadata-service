from flask_restful import Resource, reqparse
from common import parse_csv_b64_str_to_list

class Upload(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file',
                            type=str,
                            help='Base64 encoded csv file',
                            required=True,
                            location='json')
        self.req_parses = parser

    def get(self):
        return {'upload': 'success'}

    def post(self):
        b64_csv_file = self.req_parses.parse_args(strict=True).get('file', None)
        parse_csv_b64_str_to_list(b64_csv_file)

        return {"sent": "got"}