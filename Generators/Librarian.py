import random


class LibrarianGenerator:
    def __init__(self):
        self.byte_sequence = ""
        self.text = ""
        with open("../Text for Librarian generator.txt", 'r', encoding='utf-8') as file:
            self.text = ''.join(filter(lambda x: x.isalpha(), file.read()))

    def generate_byte_sequence(self, length=None):
        for char in self.text:
            byte_representation = bin(ord(char))[2:].zfill(8)
            self.byte_sequence += byte_representation
        if length is None or length > len(self.byte_sequence):
            return self.byte_sequence
        else:
            start_index = random.randint(0, len(self.byte_sequence) - length)
            return self.byte_sequence[start_index:start_index+length]

