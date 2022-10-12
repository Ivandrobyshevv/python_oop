class Car:
    """Базовый класс машина"""

    def __init__(self, speed, color, name, is_police: bool = False):
        """Инициализация класса"""
        self.speed = speed
        self.color = color
        self.name = name
        self._is_police = is_police

    def go(self):
        return f'Машина {self.name} {self.color} цвета поехала'

    def stop(self):
        return f'Машина {self.name} {self.color} цвета остановилась'

    def turn(self, side: str):
        return f'Машина {self.name} {self.color} повернула на {side}'

    def show_speed(self):
        return f'Машина {self.name} {self.color} едет со скоростью {self.speed} км/ч'


class TownCar(Car):
    """Класс городская машина"""

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            return f'Машина {self.name} {self.color} цвета превысила скорость на {self.speed - 60}'
        else:
            return f'Машина {self.name} {self.color} едет со скоростью {self.speed} км/ч'


class SportCar(Car):
    """Класс спорткар"""

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)


class WorkCar(Car):
    """Класс рабочая машина"""

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            return f'Машина {self.name} {self.color} цвета превысила скорость на {self.speed - 60} км/ч'
        else:
            return f'Машина {self.name} {self.color} едет со скоростью {self.speed} км/ч'


class PoliceCar(Car):
    """Класс полицейская машина"""
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, is_police=True)

    def show_speed(self):
        return f'Полицейская машина {self.name} {self.color} едет со скоростью {self.speed} км/ч'


# Test1
town_car = TownCar(50, 'black', 'MINI Cooper Hardtop')
print(town_car.name)  # MINI Cooper Hardtop
print(town_car.color)  # black
print(town_car.go())  # Машина MINI Cooper Hardtop black цвета поехала
print(town_car.turn('лево'))  # Машина MINI Cooper Hardtop black повернула на лево
print(town_car.show_speed())  # Машина MINI Cooper Hardtop black едет со скоростью 50 км/ч
print(town_car.stop())  # Машина MINI Cooper Hardtop black цвета остановилась
# Test2
sport_car = SportCar(150, 'white', 'Porsche 911')
print(sport_car.name)  # Porsche 911
print(sport_car.color)  # white
print(sport_car.go())  # Машина Porsche 911 white цвета поехала
print(sport_car.turn('право'))  # Машина Porsche 911 white повернула на право
print(sport_car.show_speed())  # Машина Porsche 911 white едет со скоростью 150 км/ч
print(sport_car.stop())  # Машина Porsche 911 white цвета остановилась
# Test3
work_car = WorkCar(70, 'red', 'Audi Q3')
print(work_car.name)  # Audi Q3
print(work_car.color)  # red
print(work_car.go())  # Машина Audi Q3 red цвета поехала
print(work_car.turn('право'))  # Машина Audi Q3 red повернула на право
print(work_car.show_speed())  # Машина Audi Q3 red цвета превысила скорость на 10 км/ч
print(work_car.stop())  # Машина Audi Q3 red цвета остановилась

# Test4
police_car = PoliceCar(60, 'white with blue stripes', 'BMW 3')
print(police_car.name)  # BMW 3
print(police_car.color)  # white with blue stripes
print(police_car.go())  # Машина BMW 3 white with blue stripes цвета поехала
print(police_car.turn('право'))  # Машина BMW 3 white with blue stripes повернула на право
print(police_car.show_speed())  # Машина BMW 3 white with blue stripes едет со скоростью 60 км/ч
print(police_car.stop())  # Машина BMW 3 white with blue stripes цвета остановилась
