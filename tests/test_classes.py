from datetime import datetime
import pytest
from classes import Operation


@pytest.mark.parametrize("input_date, expected_results", [("2019-07-03T18:35:29.512364", "03.07.2019")])
def test_Opertation_get_convert_date(input_date, expected_results):
    operation = Operation(input_date, "", "", "", "", "")
    assert operation.get_convert_date() == expected_results
    assert operation.get_datetime() == datetime.strptime(input_date, '%Y-%m-%dT%H:%M:%S.%f')


def test_Operation_get_description():
    operation = Operation("2019-01-01T00:00:00.000000", "Перевод организации", "", "", "", "")
    assert operation.get_description() == "Перевод организации"


@pytest.mark.parametrize("input_from, expected_results_from, input_to, expected_results_to", [
    ("Счет 26406253703545413262", "Счет **3262", "Счет 20735820461482021315", "Счет **1315"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758", "Visa Platinum 8990922113665229",
     "Visa Platinum 8990 92** **** 5229"),
    (None, "Нет данных", "Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229")
])
def test_get_from_and_get_to(input_from, expected_results_from, input_to, expected_results_to):
    operation = Operation("2019-01-01T00:00:00.000000", "", input_from, input_to, "", "")
    assert operation.get_from() == expected_results_from
    assert operation.get_to() == expected_results_to


def test_get_amount():
    operation = Operation("2019-01-01T00:00:00.000000", "", "", "", "40701.91", "USD")
    assert operation.get_amount() == "40701.91 USD"


