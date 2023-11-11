import random


class Lehmer:
    def __init__(self, seed=None, a=2 ** 16 + 1, m=2 ** 32, c=119):
        if seed is None:
            # seed = random.randint(0, m - 1)
            seed = 2
        self.seed = seed
        self.a = a
        self.m = m
        self.c = c

    def generate_lehmer_low(self, length):
        result = ""

        while len(result) < length:
            self.seed = (self.a * self.seed + self.c) % self.m
            bin_seed = bin(self.seed)[2:]
            if len(bin_seed) < 32:
                bin_seed = bin_seed.zfill(32)
            result += bin_seed[-8:]  # Молодші 8 біт

        while len(result) > length:
            result = result[:-1]

        return result

    def generate_lehmer_high(self, length):
        result = ""

        while len(result) < length:
            self.seed = (self.a * self.seed + self.c) % self.m
            bin_seed = bin(self.seed)[2:]
            if len(bin_seed) < 32:
                bin_seed = bin_seed.zfill(32)
            result += bin_seed[:8]  # Старші 8 біт

        while len(result) > length:
            result = result[:-1]

        return result


lehmer = Lehmer()
print(lehmer.generate_lehmer_low(16))

