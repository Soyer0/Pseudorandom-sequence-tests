import random


class L20:
    def __init__(self):
        self.seed = ""
        while '1' not in self.seed:
            self.seed = ''.join(random.choice('01') for _ in range(20))

    def generate(self, length):
        result = ""
        for _ in range(length):
            result += self.seed[0]
            new_bit = int(self.seed[17]) ^ int(self.seed[15]) ^ int(self.seed[11]) ^ int(self.seed[0])
            self.seed = self.seed[1:] + str(new_bit)
        return result
