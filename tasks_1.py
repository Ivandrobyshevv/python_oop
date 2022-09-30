class Counter:
    """Подсчитывает значение"""

    def __init__(self, value=0) -> None:
        self.value = value

    def increment(self) -> None:
        """Увеличивает значение на 1"""
        self.value += 1

    def display(self) -> None:
        """Печатает текущее значение счетчика"""
        print(f'Текущее значение счетчика = {self.value}')

    def reset(self) -> None:
        """Обнуляет значение"""
        self.value = 0


class Point:
    """Подсчет расстояния между 2 точками по теореме Пифагора"""

    def __init__(self, cord_x=0, cord_y=0) -> None:
        self.x = cord_x
        self.y = cord_y

    def get_distance(self, odj) -> int:
        """Расчет расстояния"""
        if not isinstance(odj, Point):
            raise ValueError("Передана не точка")

        distance = ((self.x - odj.x) ** 2 + (self.y - odj.y) ** 2) ** 0.5
        return distance
