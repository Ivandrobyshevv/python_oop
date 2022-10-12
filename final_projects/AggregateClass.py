
class AggregateBase:
    def __init__(self):
        self.numbers = list()

    def add_number(self, value):
        self.numbers.append(value)


class MinStat(AggregateBase):

    def result(self):
        if len(self.numbers) < 1:
            return None
        return min(self.numbers)


class MaxStat(AggregateBase):
    def result(self):
        if len(self.numbers) < 1:
            return None
        return max(self.numbers)


class AverageStat(AggregateBase):
    def result(self):
        if len(self.numbers) < 1:
            return None
        return sum(self.numbers) / len(self.numbers)


values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
avg = AverageStat()

for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    avg.add_number(v)

print(mins.result(), maxs.result(), avg.result())
