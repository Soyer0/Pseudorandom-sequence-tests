import random


class Geffe:
    def __init__(self):
        self.l9_seed = self.l10_seed = self.l11_seed = ""
        while '1' not in self.l9_seed:
            self.l9_seed = ''.join(random.choice('01') for _ in range(20))
        while '1' not in self.l10_seed:
            self.l10_seed = ''.join(random.choice('01') for _ in range(20))
        while '1' not in self.l11_seed:
            self.l11_seed = ''.join(random.choice('01') for _ in range(20))

    def generate_l9_bit(self):
        new_bit = int(self.l9_seed[0]) ^ int(self.l9_seed[1]) ^ int(self.l9_seed[3]) ^ int(self.l9_seed[4])
        self.l9_seed = self.l9_seed[1:] + str(new_bit)

    def generate_l10_bit(self):
        new_bit = int(self.l10_seed[0]) ^ int(self.l10_seed[3])
        self.l10_seed = self.l10_seed[1:] + str(new_bit)

    def generate_l11_bit(self):
        new_bit = int(self.l11_seed[0]) ^ int(self.l11_seed[2])
        self.l11_seed = self.l11_seed[1:] + str(new_bit)

    def generate_bit(self, length):
        result = ""
        for _ in range(length):
            x = int(self.l11_seed[0])
            y = int(self.l9_seed[0])
            s = int(self.l10_seed[0])
            result += str(s ^ (x ^ (1 ^ s) & y))
            self.generate_l11_bit()
            self.generate_l9_bit()
            self.generate_l10_bit()

        return result

