class Vector:
    def __init__(self, *args):
        digits = [i for i in args if isinstance(i, int)]
        self.values = sorted(digits)

    def __str__(self):
        if self.values:
            return f'Вектор({",".join([str(i) for i in self.values])})'
        else:
            return f'Вектор пуст'

    def __add__(self, other):
        if r := self.__other_is_digit(other, '+'):
            return r
        elif r := self.__other_is_class(other, '+'):
            return r
        else:
            raise ValueError(f'Вектор нельзя умножить на {other}')

    def __mul__(self, other):
        if r := self.__other_is_digit(other, '*'):
            return r
        elif r := self.__other_is_class(other, '*'):
            return r
        else:
            raise ValueError(f'Вектор нельзя умножить на {other}')

    def __other_is_class(self, other: object, operator: str):
        """Проверка на класс"""
        if isinstance(other, Vector) and len(other.values) == len(self.values):
            if operator == "+":
                values = [i + j for i, j in zip(self.values, other.values)]
                return Vector(*values)
            elif operator == "*":
                values = [i + j for i, j in zip(self.values, other.values)]
                return Vector(*values)
        else:
            return False

    def __other_is_digit(self, other: int, operator: str):
        """Проверка на цифру"""
        if isinstance(other, int):
            if operator == '+':
                values = [i + other for i in self.values]
                return Vector(*values)
            elif operator == '*':
                values = [i * other for i in self.values]
                return Vector(*values)
        else:
            return False


# Tests
d1 = Vector('f', 'd', 1)
print(d1)  # Вектор(1)

v1 = Vector(1, 2, 3)
print(v1)  # "Вектор(1,2,3)

v2 = Vector(3, 4, 5)
print(v2)  # Вектор(3,4,5)

v3 = v1 + v2
print(v3)  # Вектор(9,11,13)

v4 = v3 + 5
print(v4)  # Вектор(9,11,13)

v5 = v1 * 2
print(v5)  # Вектор(2,4,6)

v6 = v5 + 'hi'
print(v6)  # ValueError: Вектор нельзя умножить на hi
