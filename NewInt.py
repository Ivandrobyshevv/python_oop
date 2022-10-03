class NewInt(int):

    def repeat(self, count=2):
        return int(str(self) * count)

    def to_bin(self):
        return int(bin(self)[2:])

