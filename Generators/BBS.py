import random


class BBS:
    def __init__(self):
        self.p = int("D5BBB96D30086EC484EBA3D7F9CAEB07", 16)
        self.q = int("425D2B9BFDB25B9CF6C416CC6E37B59C1F", 16)
        self.n = self.p * self.q
        self.r = random.randint(2, self.n - 1)

    def next_r(self):
        self.r = pow(self.r, 2, self.n)

    def generate_bit_sequence(self, length):
        generated_sequence = ""
        for _ in range(length):
            self.next_r()
            if self.r % 2 == 0:
                generated_sequence += '0'
            else:
                generated_sequence += '1'
        return generated_sequence

    def generate_byte_sequence(self, length):
        generated_sequence = ""
        while len(generated_sequence) < length:
            self.next_r()
            generated_sequence += bin(self.r % 256)[2:].zfill(8)
        while len(generated_sequence) > length:
            generated_sequence = generated_sequence[:-1]
        return generated_sequence
