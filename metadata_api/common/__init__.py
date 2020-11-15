import csv, io, base64
from metadata import mongo
import pandas as pd


server_error_responce_500 = {
    "data": {
        "message": "server error"
    },
    "response": {
        "code": "500",
        "status": "server error"
    }
}


def parse_csv_b64_str_to_list(b64_str):
    """
    Function used to parse base64 encoded string (representing csv file)
    in python dict.

    :param b64_str: base64 encoded string
    :return: dict
    """
    csv_file_data = io.StringIO(base64.b64decode(b64_str).decode())

    reader = csv.DictReader(csv_file_data)
    dict_list = []
    for line in reader:
        dict_list.append(line)

    csv_file_data.close()

    return dict_list


def _update_db(entries):
    """
    Function used to insert data to mongoDB.
    To insert data an iswc No must be provided.

    :param entries: dict
    :return: dict of inserted data , int of skipped entries
    """
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
    """
    Function used to querry mongoDB.

    :param iswc: list of iswc No
    :return: list
    """
    result = list(mongo.db.music.find({'iswc': {'$in': iswc}}))
    list(map(lambda x: str(x.pop('_id')), result))

    return result


def insert_to_db(entries):
    """
    Function used to update mongoDB.
    An iswc No must be provided with each entry.

    :param entries: list of data
    :return: list of inserted data and number of skipped
    """
    added, skipped = _update_db(entries)

    return _query_db(added), skipped


def _query_db_concate(iswc):
    """
    Function used to concat contributors, source and id.

    :param iswc: list of iswc No.
    :return: list of concated data
    """
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


def query_to_base64_csv(iswc):
    """
    Function used to retrieve mongoDB data and encode it in 
    base64 string representing a csv file. 
    
    :param iswc: list of iswc No
    :return: string base64 encoded csv
    """
    s_buf = io.StringIO()
    data = _query_db_concate(iswc)
    df = pd.DataFrame(data)
    res_df = df.set_index('iswc')
    res_df.to_csv(s_buf)

    res = s_buf.getvalue()
    s_buf.close()

    b64_res = base64.b64encode(res.encode("utf-8")).decode()
    return b64_res


