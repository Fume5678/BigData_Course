import unittest

def calculate(inp):
    args = inp.split(" ")
    a = int(args[0])
    ops = args[1]
    b = int(args[2])

    if ops == "+":
        return a + b
    if ops == "-":
        return a - b
    if ops == "/":
        return a / b
    if ops == "//":
        return a // b
    if ops == "**":
        return a ** b



class test_calculate(unittest.TestCase):
    def test_operation(self):
        self.assertEqual(5, calculate("3 + 2"))
        self.assertEqual(1, calculate("3 - 2"))
        self.assertEqual(2, calculate("4 / 2"))
        self.assertEqual(3, calculate("7 // 2"))
        self.assertEqual(25, calculate("5 ** 2"))



