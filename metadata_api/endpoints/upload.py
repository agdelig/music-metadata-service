from flask_restful import Resource, reqparse
from common import _parse_csv_b64_str_to_list, _insert_to_db


class Upload(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file',
                            type=str,
                            help='Base64 encoded csv file',
                            required=True,
                            location='json')
        self.req_parses = parser

    def post(self):
        b64_csv_file = self.req_parses.parse_args(strict=True).get('file', None)
        entries = _parse_csv_b64_str_to_list(b64_csv_file)
        result, skipped = _insert_to_db(entries)

        return {
            'data': result,
            'skipped': str(skipped),
            'responce': {
                'code': '200',
                'status': 'success'
            }
        }
