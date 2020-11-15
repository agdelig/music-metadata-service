from flask_restful import Resource, reqparse
from common import query_to_base64_csv, server_error_responce_500


incorrect_request = {
    "data": {
        "message": "iswc is incorrect or does not exist"
    },
    "response": {
        "code": "404",
        "status": "client error"
    }
}


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
        try:
            file = query_to_base64_csv(iswcs)
        except KeyError:
            return incorrect_request, 404
        except Exception:
            return server_error_responce_500, 500

        return{
            'file': file,
            'responce': {
                'code': '200',
                'status': 'success'
            }
        }
