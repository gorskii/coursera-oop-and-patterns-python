from unittest import TestCase
from w2.screen import Vec2d


class TestVec2d(TestCase):
    def test_addition(self):
        vector1 = Vec2d(2.0, 3.0)
        vector2 = Vec2d(3.0, 4.0)
        expected = Vec2d(5.0, 7.0)
        self.assertEqual(vector1 + vector2, expected)

    def test_subtraction(self):
        vector1 = Vec2d(3.0, 4.0)
        vector2 = Vec2d(1.0, 2.0)
        expected = Vec2d(2.0, 2.0)
        self.assertEqual(vector1 - vector2, expected)

    def test_multiplication(self):
        vector = Vec2d(3.0, 4.0)
        number = 3
        expected = Vec2d(9.0, 12.0)

        with self.subTest('vector * number'):
            self.assertEqual(vector * number, expected)

        with self.subTest('number * vector'):
            self.assertEqual(number * vector, expected)

    def test_equality(self):
        vector1 = Vec2d(3.0, 4.0)
        vector2 = Vec2d(3.0, 4.0)
        self.assertTrue(vector1 == vector2)

    def test_operations_with_invalid_types(self):
        vector1 = Vec2d(2.0, 3.0)
        other = 'string'
        vector2 = Vec2d(3.0, 3.0)

        with self.subTest(case='add'):
            with self.assertRaises(TypeError):
                vector1 + other

        with self.subTest(case='sub'):
            with self.assertRaises(TypeError):
                vector1 - other

        with self.subTest(case='mul'):
            with self.assertRaises(TypeError):
                vector1 * other

        with self.subTest(case='multiply by vector'):
            with self.assertRaises(TypeError):
                vector1 * vector2

        with self.subTest(case='eq'):
            self.assertFalse(vector1 == other)

    def test_return_int_pair(self):
        vector = Vec2d(4.7, 2.3)
        expected = (4, 2)
        self.assertEqual(vector.int_pair(), expected)

    def test_length(self):
        cases = (
            Vec2d(12.0, 5.0),
            Vec2d(2.0, 5.0),
            Vec2d(12.0, -2.0)
        )
        expected_results = (
            13,
            5,
            12,
        )
        for vector, expected in zip(cases, expected_results):
            with self.subTest(case=vector):
                self.assertEqual(len(vector), expected)
