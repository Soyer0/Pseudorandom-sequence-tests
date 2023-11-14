import random


class L89:
    def __init__(self):
        self.seed = ""
        while '1' not in self.seed:
            self.seed = ''.join(random.choice('01') for _ in range(89))

    def generate(self, length):
        result = ""
        for _ in range(length):
            result += self.seed[0]
            new_bit = int(self.seed[51]) ^ int(self.seed[0])
            self.seed = self.seed[1:] + str(new_bit)
        return result
