import json

with open('operations.json', 'r', encoding="utf8") as json_file:
    data = json.load(json_file)


def get_transaction():
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
    if 'Счет' in card:
        return card[:4] + ' **' + card[-4:]
    else:
        name = card[:-16]
        nums = card[-16:]
        nums = nums.replace(card[-10:-4], '******')
        format_nums = ''
        for i in range(0, len(nums), 4):
            format_nums += nums[i:i + 4] + ' '
        return name + ' ' + format_nums
