class Person:
    def __init__(self, name: str, patronymic: str, surname: str, dict_numbers: dict):
        self.name = name.title()
        self.surname = surname.title()
        self.patronymic = patronymic.title()
        self.dict_numbers = dict_numbers

    def get_phone(self):
        return self.dict_numbers.get('private', None)

    def get_name(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    def get_work_phone(self):
        return self.dict_numbers.get('work', None)

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.surname}! Примите участие в нашем беспроигрышном конкурсе' \
               f' для физических лиц'


class Company:
    def __init__(self, name_company: str, type_company: str, dict_numbers: dict, *args):
        self.name_company = name_company
        self.dict_numbers = dict_numbers
        self.type_company = type_company
        self.persons = args

    def get_phone(self):
        if bool(self.dict_numbers.get('contact', 0)):
            return self.dict_numbers['contact']

        for person in self.persons:
            if not person.dict_numbers.get('work', None) is None:
                return person.dict_numbers['work']

    def get_name(self):
        return self.name_company.title()

    def get_sms_text(self):
        return f'Для компании {self.name_company} есть супер предложение!' \
               f'Примите участие в нашем беспроигрышном конкурсе для {self.type_company}'


def send_sms(*args):
    for obj in args:
        if bool(obj.get_phone()):
            rez = obj.get_phone()
            print(f"Отправлено СМС на номер {rez} с тексом {obj.get_sms_text()}")
        else:
            print(f'Не удалось отправить сообщение абоненту: {obj.get_name()}')


# TEST
person1 = Person('Ivan', 'Ivanovich', 'Ivanov', {"private": 123, "work": 456})
person2 = Person('Ivan', "Petrovich", 'Petrov', {'private': 789})
person3 = Person("ivan", 'Petrovich', 'Sidorov', {'work': 789})
person4 = Person("John", "Unknown", 'Doe', {})
company1 = Company("Bell", "OOO", {'contact': 111}, person3, person4)
company2 = Company("Cell", "AO", {"non_contact": 222}, person2, person3)
company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)
"""
Отправлено СМС на номер 123 с тексом Уважаемый Ivan Ivanov! Примите участие в нашем беспроигрышном конкурсе для физических лиц
Отправлено СМС на номер 789 с тексом Уважаемый Ivan Petrov! Примите участие в нашем беспроигрышном конкурсе для физических лиц
Не удалось отправить сообщение абоненту: Sidorov Ivan Petrovich
Не удалось отправить сообщение абоненту: Doe John Unknown
Отправлено СМС на номер 111 с тексом Для компании Bell есть супер предложение!Примите участие в нашем беспроигрышном конкурсе для OOO
Отправлено СМС на номер 789 с тексом Для компании Cell есть супер предложение!Примите участие в нашем беспроигрышном конкурсе для AO
Не удалось отправить сообщение абоненту: Dell
"""
