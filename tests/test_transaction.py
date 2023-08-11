from src.transaction import Transactions

transaction = {
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


def test_class_transaction():
    a = Transactions(transaction)
    assert str(a) == "13.07.2019 Перевод с карты на счет\n" \
                     "Maestro 1308 79** **** 7170 -> Счет **8612\n" \
                     "97853.86 руб."
