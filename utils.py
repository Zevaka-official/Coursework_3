import json


def load_file(filename):
    '''

    :param filename: имя файла json
    :return: возвращает список
    '''
    with open(filename, encoding="UTF-8", mode="r") as f:
        return json.load(f)


def get_executed(operation_list):
    '''

    :param operation_list: список
    :return: выполненные операции
    '''
    operation_list = [op for op in operation_list if op and op["state"] == "EXECUTED"]
    return operation_list

