class Notebook:
    def __init__(self, *args):
        self.__notes = list(*args)

    def notes_list(self):
        """Сортирует и выводит список"""
        sort_notes_list = sorted(self.__notes)
        for _ in range(len(sort_notes_list)):
            print(_ + 1, '.', sort_notes_list[_])


class Money:
    def __init__(self, dollars, cents):
        self.__dollars = dollars
        self.__cents = cents
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        """Вывод кол-во долларов"""
        return self.__dollars

    @dollars.setter
    def dollars(self, new_value: int):
        """Изменение кол-во долларов"""
        if isinstance(new_value, int) and new_value >= 0:
            self.__dollars = new_value
            self.total_cents = new_value * 100 + self.__cents
        else:
            print("Error dollars")

    @property
    def cents(self):
        """Вывод кол-во центов"""
        return self.__cents

    @cents.setter
    def cents(self, new_value: int):
        """Изменение кол-во центов"""
        if isinstance(new_value, int) and new_value >= 0:
            self.__cents = new_value
            self.total_cents = self.__dollars + new_value
        else:
            print("Error cents")

    def __str__(self):
        return f'Выше состояние составляет {self.__dollars} долларов {self.__cents} центов'
