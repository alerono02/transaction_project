from datetime import datetime

from src.funcs import get_masking_card


class Transactions:

    def __init__(self, transaction: dict):
        """
        Инициализация транзакции
        :param transaction:
        """
        self.transaction = transaction
        self.date = self.transaction['date']
        self.description = self.transaction['description']
        self.operation_from = self.transaction["from"]
        self.operation_to = self.transaction['to']
        self.operationAmount = self.transaction['operationAmount']

    def get_format_date(self):
        """
        Форматирует дату в нужный вид
        :return: formatted date
        """
        date = datetime.fromisoformat(self.date)
        formatted_date = date.strftime("%d.%m.%Y")
        return formatted_date

    def get_amount(self):
        return self.operationAmount['amount'] + ' ' + self.operationAmount['currency']['name']

    def __repr__(self):
        date = self.get_format_date()
        amount = self.get_amount()
        return "{date} {description}\n" \
               "{from_card} -> {to_card}\n" \
               "{amount}".format(date=date,
                                 description=self.description,
                                 from_card=get_masking_card(self.operation_from),
                                 to_card=get_masking_card(self.operation_to),
                                 amount=amount)
