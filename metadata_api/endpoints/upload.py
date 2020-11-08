from flask_restful import Resource, reqparse
import base64


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

        csv_file = base64.b64decode(b64_csv_file)

        csv1 = base64.b64decode(b64_csv_file).decode('utf-8').split(',')
        for v in csv1:
            print(v)

        import csv, io

        freader = csv.reader(io.StringIO(csv_file.decode()))
        print(type(csv_file.decode()))
        reader = csv.DictReader(freader, 'rU')
        dict_list = []

        for line in reader:
            dict_list.append(line)
        print(dict_list)

        return {"sent": "got"}