from string import digits, ascii_letters


class Registration:
    def __init__(self, login, password):
        self.__login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login: str):
        if not login.count('@') > 0:
            raise ValueError("Login must include at least one '@'")
        if not login[login.find('@'):-1]:
            raise ValueError("Login must include at least one '.'")

        self.__login = login

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password):
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть строкой")
        if not 4 < len(password) < 12:
            raise ValueError('Пароль должен быть длиннее 4х и меньше 12 символов')
        if not self.is_include_digit(password):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        if not self.is_include_all_register(password):
            raise ValueError("Пароль должен содержать хотя бы 2 заглавные буквы")
        if not self.is_include_only_latin(password):
            raise ValueError("Пароль должен содержать только латинский алфавит")
        if not self.check_password_dictionary(password):
            raise ValueError("Ваш пароль содержится в списке самых легких ")
        self.password = password

    @staticmethod
    def check_password_dictionary(password):
        with open('easy_passwords.txt') as file:
            data = file.read().split('\n')
        for d in data:
            if d == password:
                return False
        return True

    @staticmethod
    def is_include_only_latin(password: str):
        for word in password:
            if word not in ascii_letters+digits:
                return False
        return True

    @staticmethod
    def is_include_all_register(password: str):
        count_upper = 0
        for i in password:
            if i.isupper():
                count_upper += 1
                if count_upper > 1:
                    return True
        return False

    @staticmethod
    def is_include_digit(password):
        for digit in digits:
            if digit in password:
                return True
        return False
