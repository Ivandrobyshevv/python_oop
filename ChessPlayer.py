"""Сравнение шахматистов между собой"""


class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        return self.__check_type_other(other, '=')

    def __gt__(self, other):
        return self.__check_type_other(other, '>')

    def __lt__(self, other):
        return self.__check_type_other(other, "<")

    def __check_type_other(self, other, operator):
        if isinstance(other, int):
            if operator == '=':
                return self.rating == other
            elif operator == '>':
                return self.rating > other
            else:
                return self.rating < other
        elif isinstance(other, ChessPlayer):
            if operator == '=':
                return self.rating == other.rating
            elif operator == '>':
                return self.rating > other.rating
            else:
                return self.rating < other.rating
        else:
            return f'Невозможно выполнить сравнение'


# Tests
magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 400)  # False
print(ian == 2789)  # True
print(magnus == ian)  # False
print(magnus > ian)  # True
print(magnus < ian)  # False
print(magnus < [1, 2])  # Невозможно выполнить сравнение
