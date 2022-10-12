class FoodInfo:
    def __init__(self, proteins: int = 0, fats: int = 0, carbohydrates: int = 0):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def get_proteins(self):
        """Возвращает кол-во белков"""
        return f'Белки: {self.proteins}'

    def get_fats(self):
        """Возвращает кол-во жиров"""

        return f'Жиры: {self.fats}'

    def get_carbohydrates(self):
        """Возвращает кол-во углеводов"""
        return f'Углеводы: {self.carbohydrates}'

    def det_kcalories(self):
        """Возвращает общую калорийность"""
        return f'Общая калорийность: {(self.fats * 9) + (self.proteins * 4) + (self.carbohydrates * 4)}'

    def __add__(self, other):
        """Складывает экземпляры и возвращает новый класс """
        if not isinstance(other, FoodInfo):
            raise "Вы складываете не экземпляр класса"
        proteins = self.proteins + other.proteins
        fats = self.fats + other.fats
        carbohydrates = self.carbohydrates + other.carbohydrates
        return FoodInfo(proteins, fats, carbohydrates)


# Tests
food1 = FoodInfo(100, 100, 100)
food2 = FoodInfo(50, 60, 70)
food3 = food1 + food2

# Белки: 100 Жиры: 100 Углеводы: 100 Общая калорийность: 1700
print(food1.get_proteins(), food1.get_fats(),
      food1.get_carbohydrates(), food1.det_kcalories())

# Белки: 50 Жиры: 60 Углеводы: 70 Общая калорийность: 1020
print(food2.get_proteins(), food2.get_fats(),
      food2.get_carbohydrates(), food2.det_kcalories())

# Белки: 150 Жиры: 160 Углеводы: 200 Общая калорийность: 2840
print(food3.get_proteins(), food3.get_fats(),
      food3.get_carbohydrates(), food3.det_kcalories())
