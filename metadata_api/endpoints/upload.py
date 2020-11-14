from flask_restful import Resource, reqparse
from common import parse_csv_b64_str_to_list
from metadata import mongo


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
        entries = parse_csv_b64_str_to_list(b64_csv_file)
        result, skipped = db_update(entries)

        return {
            "sent": "got",
            'data': result,
            'skipped': str(skipped)
        }


def db_update(entries):
    added = []
    skipped = 0
    for e in entries:
        if len(e['iswc']) == 0:
            skipped += 1
            continue

        added.append(e['iswc'])

        entry_contributors = str.split(e.pop('contributors'), '|')
        entry_sources = [
            {
                'source': e.pop('source'),
                'id': e.pop('id')
            }
        ]
        mongo.db.music.update({'iswc': e['iswc']},
                              {
                                  '$setOnInsert': e,
                                  '$push': {
                                      'contributors': {
                                          '$each': entry_contributors
                                      },
                                      'sources': {
                                          '$each': entry_sources
                                      }
                                  }
                              }, upsert=True)

    result = list(mongo.db.music.find({'iswc': {'$in': added}}))
    list(map(lambda x: str(x.pop('_id')), result))

    return result, skipped
