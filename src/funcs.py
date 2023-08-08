import json

with open('operations.json', 'r', encoding="utf8") as json_file:
    data = json.load(json_file)


def get_transaction(data_):
    """
    Получает на вход список операций и
    возвращает 5 последних успешных
    :param data_:
    :return:
    """
    executed_list = []
    for trans in reversed(data_):
        if len(executed_list) < 5:
            if trans['state'] == "EXECUTED":
                executed_list.append(trans)
        else:
            return executed_list
