import unittest

class Circle:
    def __init__(self, r):
        self.r = r
        self.pi = 3.14

    def get_square(self):
        return self.r**2 * self.pi

    def get_name(self):
        return "circle"


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_square(self):
        return self.a * self.b

    def get_name(self):
        return "rectangle"


class Triangle:
    def __init__(self, h, b):
        self.h = h
        self.b = b

    def get_square(self):
        return 0.5 * self.h * self.b

    def get_name(self):
        return "triangle"


def square(figure):
    res = {
        "name": figure.get_name(),
        "area": figure.get_square()
    }

    return res


class test_area(unittest.TestCase):
    def test_circle(self):
        res = square(Circle(3))
        self.assertEqual(res["name"], "circle")
        self.assertAlmostEqual(res["area"], 28.26, places=2)

    def test_rect(self):
        res = square(Rect(3, 4))
        self.assertEqual(res["name"], "rectangle")
        self.assertEqual(res["area"], 12)

    def test_triangle(self):
        res = square(Triangle(3, 6))
        self.assertEqual(res["name"], "triangle")
        self.assertEqual(res["area"], 9)

