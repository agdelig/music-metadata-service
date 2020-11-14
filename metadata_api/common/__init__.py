import csv, io, base64


def parse_csv_b64_str_to_list(b64_str):
    csv_file_data = io.StringIO(base64.b64decode(b64_str).decode())

    reader = csv.DictReader(csv_file_data)
    dict_list = []
    for line in reader:
        dict_list.append(line)

    return dict_list


