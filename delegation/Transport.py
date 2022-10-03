class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f'Тип транспорта {self.kind} марка {self.brand} может развить скорость {self.max_speed} км/ч'


class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_reside):
        super().__init__(brand, max_speed, kind=Car.__name__)
        self.mileage = mileage
        self.__gasoline_reside = gasoline_reside

    @property
    def gasoline(self):
        return f'Осталось бензина на {self.__gasoline_reside}'

    @gasoline.setter
    def gasoline(self, value):
        if isinstance(value, int):
            self.__gasoline_reside += value
            print(f'Объем топлива увеличен на {value}л и составляет {self.__gasoline_reside}л.')
        else:
            print('Ошибка заправки автомобиля')


class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind=Boat.__name__)
        self.owners_name = owners_name

    def __str__(self):
        return f'Это лодка марки {self.brand} владеет {self.owners_name}'


class Plane(Transport):
    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind=Plane.__name__)
        self.capacity = capacity

    def __str__(self):
        return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'


# Tests
transport = Transport('Telega', 10)
print(transport)  # Тип транспорта None марка Telega может развить скорость 10
bike = Transport('shkolnik', 20, 'bike')
print(bike)  # Тип транспорта bike марка shkolnik может развить скорость 20
# 1
first_plane = Plane('Virgin Atlantic', 700, 300)
print(first_plane)  # Самолет марки Virgin Atlantic вмещает в себя 300 людей
# 2
first_car = Car('BMW', 230, 75000, 300)
print(first_car)  # Тип транспорта Car марка BMW может развить скорость 230 км/ч
print(first_car.gasoline)  # Осталось бензина на 300
first_car.gasoline = 20  # Объем топлива увеличен на 20л и составляет 320л.
print(first_car.gasoline)  # Осталось бензина на 320
# 3
second_car = Car('Audi', 230, 70000, 130)
second_car.gasoline = [None]  # Ошибка заправки автомобиля
first_boat = Boat('Yamaha', 40, 'Petr')
print(first_boat)  # Ошибка заправки автомобиля
