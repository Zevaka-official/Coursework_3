import json

from classes import Operation


def load_file(filename):
    '''

    :param filename: имя файла json
    :return: возвращает список
    '''
    with open(filename, encoding="UTF-8", mode="r") as f:
        return json.load(f)


def get_executed(operation_list:list[dict]):
    '''
    Поулчаем список ВЫПОЛНЕННЫХ операций
    :param operation_list: список словарей с данными об операции
    :return: список элементов класса Operation
    '''
    operation_list = [op for op in operation_list if op and op["state"] == "EXECUTED"]
    return [
        Operation(
            op["date"],
            op["description"],
            op["from"],
            op["to"],
            op["operationAmount"]["amount"],
            op["operationAmount"]["currency"]["name"]
        )
        for op in operation_list
    ]


def get_sorted_operations(operation_list:list[Operation]):
    '''

    :param operation_list: список элементов класса Operation
    :return: отсортированный список по дате
    '''
    return sorted(operation_list, key=lambda op: op.get_datetime(), reverse=True)

