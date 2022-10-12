from datetime import date


class Date:
    def __init__(self, month: int, day: int):
        self.month = month
        self.day = day

    def __sub__(self, other):
        if not isinstance(other, Date):
            raise f"{other} - не экземпляр класса Date"
        date1 = date(2019, self.month, self.day)
        date2 = date(2019, other.month, other.day)
        result = str(date1 - date2).split()
        return result[0] if len(result) > 1 else 0


# Test1
jan5 = Date(1, 5)
jan1 = Date(1, 1)
print(jan5 - jan1)  # 4
print(jan1 - jan5)  # -4
print(jan1 - jan1)  # 0
print(jan5 - jan5)  # 0

# Test2
mar1 = Date(3, 1)
jan1 = Date(1, 1)
print(mar1 - jan1)  # 59
print(jan1 - mar1)  # -59
print(jan1 - jan1)  # 0
print(mar1 - mar1)  # 0
