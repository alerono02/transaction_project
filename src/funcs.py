import json

with open('operations.json', 'r', encoding="utf8") as json_file:
    data = json.load(json_file)


def get_transaction(data_):
    """
    Получает на вход список транзакций и возвращает
    5 последних операций со статусом EXECUTED
    :param data_:
    :return:
    """
    executed_list = []
    while len(executed_list) != 5:
        for trans in reversed(data_):
            if trans["state"] == "EXECUTED":
                executed_list.append(trans)
    return executed_list


print(get_transaction(data))
