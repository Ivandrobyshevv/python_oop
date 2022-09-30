class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name.title()
        self.surname = surname.title()
        self.__goals = 0
        self.__assists = 0

    def score(self, goals=1):
        """Увеличивает общее кол-во забитых голов"""
        self.__goals = goals

    def maek_assist(self, assist=1):
        """Увеличивает общее кол-во сделанных передач"""
        self.__assists = assist

    def statistics(self):
        """Вывод на экран статистику"""""
        print(f'{self.surname} {self.name} - голы: {self.__goals}, передачи: {self.__assists}')


class Zebra:
    def __init__(self):
        self.__flag = 1

    def which_strip(self):
        if self.__flag:
            print('Полоска белая')
            self.__flag -= 1
        else:
            print('Полоска черная')
            self.__flag += 1


class Person:
    def __init__(self, first_name, last_name, age):
        self.full_name = f'{last_name.title()} {first_name.title()}'
        self.age = age

    def full_name(self):
        print(self.full_name)

    def is_adult(self):
        return self.age >= 18
