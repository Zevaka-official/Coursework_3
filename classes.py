import datetime


class Operation():
    def __init__(self, date, description, op_from, op_to, amount, currency):
        self.date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
        self.description = description
        self.op_from = op_from
        self.op_to = op_to
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f"{self.date} {self.description} {self.op_from} {self.op_to} {self.amount} {self.currency}"

    def get_convert_date(self):
        """

        :return: возвращает конвертированную дату
        """
        return self.date.strftime("%d.%m.%Y")

    def get_description(self):
        """

        :return: возвращает детали операции
        """
        return self.description

    @staticmethod
    def _get_from(input_str: str):
        """

        :param input_str: получает детали операции
        :return: возвращает маску операции
        """
        new_list = input_str.split()
        letters = new_list[0:-1]
        number = new_list[-1]
        if len(number) == 16:
            return f'{" ".join(letters)} {number[0:4]} {number[4:6]}** **** {number[-4:]}'
        else:
            return f'Счет **{number[-4:]}'

    def get_from(self):
        """

        :return: возвращает детали отправителя
        """
        if self.op_from is None:
            return "Нет данных"

        return Operation._get_from(self.op_from)

    def get_to(self):
        """

        :return: возвращает детали получателя
        """
        return Operation._get_from(self.op_to)

    def get_amount(self):
        """

        :return: возвращает сумму и валюту
        """
        return f'{self.amount} {self.currency}'

    def get_datetime(self):
        """

        :return: возвращает дату
        """
        return self.date
