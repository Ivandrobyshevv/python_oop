class Initialization:
    def __init__(self, capacity: int, food: list):
        if isinstance(capacity, int):
            self.capacity = capacity
            self.food = food
        else:
            print('Количество людей должно быть целым числом')


class Vegetarian(Initialization):
    def __init__(self, capacity: int, food: list):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'


class MeatEater(Initialization):
    def __init__(self, capacity: int, food: list):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} мясоедов в Москве! Они предпочитают {self.food}'


class SweetTooth(Initialization):
    def __init__(self, capacity: int, food: list):
        super().__init__(capacity, food)

    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда {self.food}'

    def __eq__(self, other):
        return self.__check_value_other(other, '=')

    def __lt__(self, other):
        return self.__check_value_other(other, '<')

    def __gt__(self, other):
        return self.__check_value_other(other, '>')

    def __check_value_other(self, other, operator):
        if isinstance(other, int):
            if operator == '=':
                return self.capacity == other
            elif operator == '>':
                return self.capacity > other
            elif operator == '<':
                return self.capacity < other
        elif isinstance(other, Initialization):
            if operator == '=':
                return self.capacity == other.capacity
            elif operator == '>':
                return self.capacity > other.capacity
            elif operator == '<':
                return self.capacity < other.capacity

        return f'Невозможно сравнить количество с {other}'


# Tests
v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом

m_first = MeatEater(15000, ['Говядина', 'рыба'])
print(m_first)  # 15000 мясоедов в Москве! Они предпочитают ['Говядина', 'рыба']

s_first = SweetTooth(30000, ['Мороженое', 'Шоколад', 'Печенье'])
print(s_first)  # Сладкоежек в Москве 30000. Их самая любимая еда ['Мороженое', 'Шоколад', 'Печенье']

print(s_first > v_first)  # True
print(30000 == s_first)  # True
print(s_first == 2500)  # False
print(1000000 < s_first)  # False
print(100 < s_first)  # True
