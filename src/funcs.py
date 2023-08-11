import json


def load_data(file):
    with open(file, 'r', encoding="utf8") as json_file:
        data = json.load(json_file)
    return data


def get_transaction(data):
    """
    Получает на вход список операций и
    возвращает 5 последних успешных
    :param:
    :return:
    """
    executed_list = []
    for trans in reversed(data):
        if len(executed_list) < 5:
            if trans['state'] == "EXECUTED" and 'from' in trans:
                executed_list.append(trans)
        else:
            return executed_list


def get_masking_card(card):
    """
    Маскирует счет или карту
    :param card:
    :return:
    """
    if 'Счет' in card:
        return card[:4] + ' **' + card[-4:]
    else:
        name = card[:-17]
        nums = card[-16:]
        nums = nums.replace(card[-10:-4], '******')
        format_nums = ''
        for i in range(0, len(nums), 4):
            format_nums += nums[i:i + 4] + ' '
        return name + ' ' + format_nums
