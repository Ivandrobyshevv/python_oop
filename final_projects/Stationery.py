class Stationery:
    def __init__(self, title, color):
        self.title = title
        self.color = color

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):
    def __init__(self, title, color, options):
        super().__init__(title, color)
        self.options = options

    def draw(self):
        return f"Пишу ручкой {self.options}, марки {self.title}, {self.color} цвет"


class Pencil(Stationery):

    def __init__(self, title, color, options):
        super().__init__(title, color)
        self.options = options

    def draw(self):
        return f"Рисую карандашом марки {self.title}, твердость грифеля - {self.options}, {self.color} цвет"


class Handle(Stationery):
    def __init__(self, title, color):
        super().__init__(title, color)

    def draw(self):
        return f"Рисую маркером марки {self.title}, {self.color} цвет"


pen = Pen('ErichKrause', 'синий', 'шариковой')
print(pen.draw())  # Пишу ручкой шариковой, марки ErichKrause, синий цвет

pencil = Pencil('ErichKrause', 'черный', 'ТМ (твёрдо-мягкий)')
print(pencil.draw())  # Рисую карандашом марки ErichKrause, твердость грифеля - ТМ (твёрдо-мягкий), черный цвет

handle = Handle('ErichKrause', 'красный')
print(handle.draw())  # Рисую маркером марки ErichKrause, красный цвет
