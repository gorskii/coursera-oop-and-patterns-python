import unittest

from w1.factorize import factorize


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        self.cases = ('string', 1.5)
        for case in self.cases:
            with self.subTest(case=case):
                self.assertRaises(TypeError, factorize, case)

    def test_negative(self):
        self.cases = (-1, -10, -100)
        for case in self.cases:
            with self.subTest(case=case):
                self.assertRaises(ValueError, factorize, case)

    def test_zero_and_one_cases(self):
        self.fail()

    def test_simple_numbers(self):
        self.fail()

    def test_two_simple_multipliers(self):
        self.fail()

    def test_many_multipliers(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()
