import base64, os
from common import _parse_csv_b64_str_to_list


class TestCsvParse:

    def test_csv_file(self):
        data = open('./tests/test_valid_file.csv', 'r').read()
        file_bytes = base64.b64encode(data.encode('UTF-8')).decode('ascii')
        file_dict = _parse_csv_b64_str_to_list(file_bytes)
        expected = [
            {'colA': 'valA1', 'colB': 'valB1'},
            {'colA': 'valA2', 'colB': 'valB2'}
        ]
        assert file_dict == expected