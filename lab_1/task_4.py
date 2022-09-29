import math
import unittest


def triangle_area(a, b, c):
    p = (a+b+c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

class test_triangle_area(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(6, triangle_area(3, 4, 5))



