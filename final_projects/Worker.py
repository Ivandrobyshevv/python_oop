SALARY = {
    'teacher': {'wage': 50_000, "bonus": 10_000},
    'programmer': {'wage': 60_000, "bonus": 5_000},
    'director': {'wage': 100_000, "bonus": 0}
}


class Worker:
    def __init__(self, name, surname, position):
        """Инициализация базового класса"""
        self.name = name
        self.surname = surname
        self.position = position
        self._income = SALARY[self.position.lower()]


class Position(Worker):

    def get_full_name(self):
        """Имя и фамилия"""
        return f'Full name: {self.surname.title()} {self.name.title()}'

    def get_total_income(self):
        """Доход (оклад+премия) """
        return f'Salary: {self._income["wage"] + self._income["bonus"]}RUB'


# Test1
person1 = Position('Abraham', 'williams', 'Teacher')
print(person1.get_full_name())  # Full name: Williams Abraham
print(person1.get_total_income())  # Salary: 60000RUB
# Test2
person2 = Position('adam', 'Peters', 'Programmer')
print(person2.get_full_name())  # Full name: Peters Adam
print(person2.get_total_income())  # Salary: 65000RUB
