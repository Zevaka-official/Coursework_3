import json

def load_file(filename):
    '''

    :param filename: имя файла json
    :return: возвращает список
    '''
    with open(filename, encoding="UTF-8", mode="r") as f:
        return json.load(f)


