class Stack:
    def __init__(self):
        self.__values = list()

    def is_empty(self):
        """Проверка стека на пустоту."""
        return not bool(self.__values)

    def push(self, item):
        """Добавляет нового элемента."""
        self.__values.append(item)

    def pop(self):
        """Возвращает верхний элемент и удаляет его"""
        if self.is_empty():
            print('Empty Stack')
        else:
            return self.__values.pop(-1)

    def peek(self):
        """Возвращает верхний элемент, не удаляет его"""
        if self.is_empty():
            print('Empty Stack')
        else:
            return self.__values[-1]

    def size(self):
        """Возвращает кол-во элементов в стеке"""
        return len(self.__values)
