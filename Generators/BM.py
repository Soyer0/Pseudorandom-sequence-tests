import math
import random


class BM:
    def __init__(self):
        self.a = int("CEA42B987C44FA642D80AD9F51F10457690DEF10C83D0BC1BCEE12FC3B6093E3", 16)
        self.p = int("5B88C41246790891C095E2878880342E88C79974303BD0400B090FE38A688356", 16)
        self.T = int('{0:b}'.format(random.getrandbits(256)), 2)

    def next_T(self):
        self.T = pow(self.a, self.T, self.p)

    def generate_bit_sequence(self, length):
        generated_sequence = ""
        for _ in range(length):
            self.next_T()
            generated_sequence += "0" if self.T < ((self.p - 1) / 2) else "1"
        return generated_sequence

    def generate_byte_sequence(self, length):
        generated_sequence = ""
        while len(generated_sequence) < length:
            self.next_T()
            k = math.floor(256 * self.T / (self.p-1))
            print(k)
            byte_k = bin(k)[2:].zfill(8)
            generated_sequence += byte_k
        while len(generated_sequence) > length:
            generated_sequence = generated_sequence[:-1]
        return generated_sequence

