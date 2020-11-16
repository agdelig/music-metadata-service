import base64, os
from common import parse_csv_b64_str_to_list


class TestCsvParse:

    def test_csv_file(self):
        data = open('./tests/test_valid_file.csv', 'r').read()
        file_bytes = base64.b64encode(data.encode('UTF-8')).decode('ascii')
        file_dict = parse_csv_b64_str_to_list(file_bytes)
        expected = [
            {'colA': 'valA1', 'colB': 'valB1'},
            {'colA': 'valA2', 'colB': 'valB2'}
        ]
        assert file_dict == expected

    def test_empty_file(self):
        data = open('./tests/empty_file.csv', 'r').read()
        file_bytes = base64.b64encode(data.encode('UTF-8')).decode('ascii')
        file_dict = parse_csv_b64_str_to_list(file_bytes)
        expected = []
        assert file_dict == expected

    def test_throws_exception(self):
        data = 'invalid base64 string'
        file_bytes = base64.b64encode(data.encode('UTF-8')).decode('ascii')
        file_dict = parse_csv_b64_str_to_list(file_bytes)
        assert len(file_dict) == 0
