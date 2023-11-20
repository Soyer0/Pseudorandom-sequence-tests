import unittest

from Tests import *
from Generators.Lehmer import *


class LehmerTest(unittest.TestCase):
    lehmer = Lehmer()
    bit_sequence = lehmer.generate_lehmer_high(16384)

    def test_equality_of_signs(self):
        alpha_001 = 0.01
        result_001 = check_equality_of_signs(self.bit_sequence, alpha_001)
        self.assertTrue(result_001)

        alpha_005 = 0.05
        result_005 = check_equality_of_signs(self.bit_sequence, alpha_005)
        self.assertTrue(result_005)

        alpha_01 = 0.1
        result_01 = check_equality_of_signs(self.bit_sequence, alpha_01)
        self.assertTrue(result_01)

    def test_independence_of_signs(self):
        alpha_001 = 0.01
        result_001 = check_independence_of_signs(self.bit_sequence, alpha_001)
        self.assertTrue(result_001)

        alpha_005 = 0.05
        result_005 = check_independence_of_signs(self.bit_sequence, alpha_005)
        self.assertTrue(result_005)

        alpha_01 = 0.1
        result_01 = check_independence_of_signs(self.bit_sequence, alpha_01)
        self.assertTrue(result_01)

    def test_homogeneity_of_bin_seq(self):
        alpha_001 = 0.01
        result_001 = check_homogeneity_of_bin_seq(self.bit_sequence, alpha_001)
        self.assertTrue(result_001)

        alpha_005 = 0.05
        result_005 = check_homogeneity_of_bin_seq(self.bit_sequence, alpha_005)
        self.assertTrue(result_005)

        alpha_01 = 0.1
        result_01 = check_homogeneity_of_bin_seq(self.bit_sequence, alpha_01)
        self.assertTrue(result_01)


if __name__ == '__main__':
    unittest.main()
