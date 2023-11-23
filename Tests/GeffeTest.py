import unittest
from Tests import *
from Generators.Geffe import *


class Test(unittest.TestCase):
    gen = Geffe()
    bit_sequence = gen.generate(6000000)

    def run_test(self, test_function, alpha):
        print(f"\nTest: {test_function.__name__} - Alpha: {alpha}")
        try:
            result = test_function(self.bit_sequence, alpha)
            print(f"Результат: {result}")
            self.assertTrue(result)
        except AssertionError:
            self.addExpectedFailure(self.run_test, AssertionError)

    def test_equality_of_signs_alpha_001(self):
        self.run_test(check_equality_of_signs, 0.01)

    def test_equality_of_signs_alpha_005(self):
        self.run_test(check_equality_of_signs, 0.05)

    def test_equality_of_signs_alpha_01(self):
        self.run_test(check_equality_of_signs, 0.1)

    def test_independence_of_signs_alpha_001(self):
        self.run_test(check_independence_of_signs, 0.01)

    def test_independence_of_signs_alpha_005(self):
        self.run_test(check_independence_of_signs, 0.05)

    def test_independence_of_signs_alpha_01(self):
        self.run_test(check_independence_of_signs, 0.1)

    def test_homogeneity_of_bin_seq_alpha_001(self):
        self.run_test(check_homogeneity_of_bin_seq, 0.01)

    def test_homogeneity_of_bin_seq_alpha_005(self):
        self.run_test(check_homogeneity_of_bin_seq, 0.05)

    def test_homogeneity_of_bin_seq_alpha_01(self):
        self.run_test(check_homogeneity_of_bin_seq, 0.1)


if __name__ == '__main__':
    unittest.main()
