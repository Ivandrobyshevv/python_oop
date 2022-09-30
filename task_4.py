class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        """Вывод email"""
        return self.__email

    def set_email(self, new_email: str):
        """Валидация и сохранение нового email"""
        if isinstance(new_email, (str,)) and new_email.count('@') == 1 and '.' in new_email[new_email.index('@'):]:
            self.__email = new_email
        else:
            print(f'ErrorMail:{new_email}')

    email = property(fget=get_email, fset=set_email)
