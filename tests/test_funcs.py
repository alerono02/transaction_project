import pytest

from src.funcs import get_transaction
from src.funcs import get_masking_card
from src.funcs import load_data


test_data = [
        {"state": "EXECUTED", "from": "12321"},
        {"state": "EXECUTED", "from": "12321"},
        {"state": "123", "from": "12321"},
        {"state": "EXECUTED", "from": "12321"},
        {"state": "EXECUTED", "from": "12321"},
        {"state": "123", "from": "12321"},
        {"state": "EXECUTED", "from": "12321"},
    ]


def test_get_transaction():
    assert get_transaction(test_data) == [
        {"state": "EXECUTED", "from": "12321"},
        {"state": "EXECUTED", "from": "12321"},
        {"state": "EXECUTED", "from": "12321"},
        {"state": "EXECUTED", "from": "12321"},
        {"state": "EXECUTED", "from": "12321"}
    ]


def test_masking():
    assert get_masking_card("Счет 59986621134048778289") == 'Счет **8289'
    assert get_masking_card("Visa Gold 1308795367077170") == 'Visa Gold 1308 79** **** 7170 '


def test_json_load():
    assert load_data("test_operations.json") == [
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612"
        }
    ]
