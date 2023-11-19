import random
from bitarray import bitarray


def str_xor(str1, str2):
    max_len = max(len(str1), len(str2))
    str1 = str1.zfill(max_len)
    str2 = str2.zfill(max_len)

    result = ''.join('1' if d1 != d2 else '0' for d1, d2 in zip(str1, str2))
    return result


def str_or(str1, str2):
    max_len = max(len(str1), len(str2))
    str1 = str1.zfill(max_len)
    str2 = str2.zfill(max_len)

    result = ''.join('1' if d1 == '1' or d2 == '1' else '0' for d1, d2 in zip(str1, str2))
    return result


class Wolfram:
    def __init__(self):
        self.seed = "1" + ''.join(random.choice('01') for _ in range(31))
        print(self.seed)

    def cyclic_shift_left(self, n):
        n = n % len(self.seed)
        return self.seed[n:] + self.seed[:n]

    def cyclic_shift_right(self, n):
        n = n % len(self.seed)
        return self.seed[-n:] + self.seed[:-n]

    def generate(self, length):
        result = ""
        for _ in range(length):
            result += self.seed[31]
            self.seed = str_xor(self.cyclic_shift_left(1), str_or(self.seed, self.cyclic_shift_right(1)))
        return result
