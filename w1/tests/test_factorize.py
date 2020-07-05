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
        self.cases = (0, 1)
        self.expected = ((0,), (1,))
        for case, result in zip(self.cases, self.expected):
            with self.subTest(case=case):
                self.assertEqual(factorize(case), result)

    def test_simple_numbers(self):
        self.cases = (3, 13, 29)
        self.expected = ((3,), (13,), (29,))
        for case, result in zip(self.cases, self.expected):
            with self.subTest(case=case):
                self.assertEqual(factorize(case), result)

    def test_two_simple_multipliers(self):
        self.cases = (6, 26, 121)
        self.expected = ((2, 3), (2, 13), (11, 11))
        for case, result in zip(self.cases, self.expected):
            with self.subTest(case=case):
                self.assertEqual(factorize(case), result)

    def test_many_multipliers(self):
        self.cases = (1001, 9699690)
        self.expected = ((7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19))
        for case, result in zip(self.cases, self.expected):
            with self.subTest(case=case):
                self.assertEqual(factorize(case), result)


if __name__ == '__main__':
    unittest.main()
