class ReversedList(object):
    def __init__(self, lst: list):
        """Инициализация класса"""
        if not isinstance(lst, list):
            raise f'TypeError(Вы передели не список - {lst})'
        self.lst = lst[::-1]

    def __len__(self):
        """Длина списка"""
        return len(self.lst)

    def __str__(self):
        return self.lst

    def __getitem__(self, item):
        """Итерация"""
        return self.lst[item]


# Test1
rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])
# Test2
rl2 = ReversedList([])
print(len(rl2))
