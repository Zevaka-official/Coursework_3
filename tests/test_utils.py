import classes
import utils
import pytest


@pytest.fixture()
def dict_fixture():
    return [{
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {
                "amount": "79931.03",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }

    ]


def test_get_executed(dict_fixture):
    op_list = utils.get_executed(dict_fixture)
    assert len(op_list) == 2
    assert type(op_list[0]) is classes.Operation


@pytest.fixture()
def operation_fixture():
    return [classes.Operation("2019-07-03T18:35:29.512364", "", "", "", "", ""),
            classes.Operation("2018-07-11T02:26:18.671407", "", "", "", "", "")]


def test_get_sorted(operation_fixture):
    sorted_list = utils.get_sorted_operations(operation_fixture)
    assert sorted_list[0].get_datetime() > sorted_list[1].get_datetime()


def test_load_file():
    assert len(utils.load_file("tests/test_operations_data.json")) == 3

