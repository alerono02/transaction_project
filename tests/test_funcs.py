from src.funcs import get_transaction

test_dict= [
    {"state": "CANCELED"},
    {"state": "EXECUTED"},
    {"state": "CANCELED"},
    {"state": "CANCELED"},
    {"state": "EXECUTED"},
    {"state": "EXECUTED"},
    {"state": "EXECUTED"},
    {"state": "EXECUTED"},
]


def test_funcs():
    assert get_transaction(test_dict) == [{"state": "EXECUTED"},
                                          {"state": "EXECUTED"},
                                          {"state": "EXECUTED"},
                                          {"state": "EXECUTED"},
                                          {"state": "EXECUTED"}]
