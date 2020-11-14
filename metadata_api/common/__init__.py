import csv, io, base64
from metadata import mongo
import pandas as pd


def _parse_csv_b64_str_to_list(b64_str):
    csv_file_data = io.StringIO(base64.b64decode(b64_str).decode())

    reader = csv.DictReader(csv_file_data)
    dict_list = []
    for line in reader:
        dict_list.append(line)

    return dict_list


def _update_db(entries):
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
                                  '$addToSet': {
                                      'contributors': {
                                          '$each': entry_contributors
                                      },
                                      'sources': {
                                          '$each': entry_sources
                                      }
                                  }
                              }, upsert=True)

    return added, skipped


def _query_db(iswc):
    result = list(mongo.db.music.find({'iswc': {'$in': iswc}}))
    list(map(lambda x: str(x.pop('_id')), result))

    return result


def _insert_to_db(entries):
    added, skipped = _update_db(entries)

    return _query_db(added), skipped


def _query_db_concate(iswc):
    query_list = _query_db(iswc)
    result = query_list.copy()

    for item in result:
        contributors = ' | '.join(item['contributors'])
        item['contributors'] = contributors
        source_list = []
        id_list = []

        for i in item['sources']:
            source_list.append(i['source'])
            id_list.append(i['id'])

        source_field = ' | '.join(source_list)
        id_field = ' | '.join(id_list)

        item.pop('sources')
        item['source'] = source_field
        item['id'] = id_field

    return result


def _query_to_base64_csv(csv_dict):
    s_buf = io.StringIO()
    data = _query_db_concate(csv_dict)
    df = pd.DataFrame(data)
    res_df = df.set_index('iswc')
    res_df.to_csv(s_buf)
    #s_buf.close()

    res = s_buf.getvalue()
    s_buf.close()

    b64_res = base64.b64encode(res.encode("utf-8")).decode()
    return b64_res


