import binascii
import random


class Librarian:
    def __init__(self):
        self.bit_sequence = ""
        self.text = ""
        with open("../Text for Librarian generator.txt", 'r', encoding='utf-8') as file:
            self.text = ''.join(filter(lambda x: x.isalpha(), file.read()))

    def generate(self, length=None):
        binary_data = self.text.encode()
        hex_representation = binascii.hexlify(binary_data)
        self.bit_sequence = bin(int(hex_representation, 16))[2:]

        if length is None or length > len(self.bit_sequence):
            return self.bit_sequence
        else:
            start_index = random.randint(0, len(self.bit_sequence) - length)
            return self.bit_sequence[start_index:start_index+length]
