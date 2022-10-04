class Road:
    """Класс для расчета массы асфальта для дороги"""
    def __init__(self, length: (int, float), width: (int, float)):
        if not isinstance(length, (int, float)):
            raise TypeError("Значение длины должны быть (int, float)")
        if not isinstance(width, (int, float)):
            raise TypeError("Значение ширины должны быть (int, float)")
        else:
            self.__length = length
            self.__width = width
            self.__asphalt_density_1m2 = 25

    def get_mass_of_asphalt(self, thickness: (float, int) = 5.0):
        """
        Инициализация класса
        :param thickness: толщина покрытия асфальта в см
        :return: float or raise
        """
        if not isinstance(thickness, (int, float)):
            raise TypeError(f"Не верное переданное значение {thickness}")
        return self.__length * self.__width * thickness * self.__asphalt_density_1m2 / 1000


def main():
    """Входная точка"""
    length = float(input("Введите длину полотна: "))
    width = float(input("Введите ширину полотна: "))
    thickness = float(input('Введите толщину полотна:'))
    road = Road(length, width)

    return round(road.get_mass_of_asphalt(thickness), 2)


if __name__ == '__main__':
    print(f'Масса асфальта - {main()}тон')
