from flask_restful import Resource, reqparse
from common import parse_csv_b64_str_to_list, insert_to_db, server_error_responce_500
from binascii import Error as binasciiError


unprocessible_entity_422 = {
    "data": {
        "message": "file upload error"
    },
    "response": {
        "code": "422",
        "status": "uprocessible entuty"
    }
}


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
        try:
            entries = parse_csv_b64_str_to_list(b64_csv_file)
            result, skipped = insert_to_db(entries)
        except binasciiError:
            return unprocessible_entity_422, 422
        except Exception:
            return server_error_responce_500, 500

        return {
            'data': result,
            'skipped': str(skipped),
            'responce': {
                'code': '201',
                'status': 'created'
            }
        }, 201
