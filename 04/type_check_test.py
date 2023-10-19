import unittest
from type_check import Integer, String, PositiveInteger

class Data:
    num = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self, num, name, price):
        self.num = num
        self.name = name
        self.price = price


class TestData(unittest.TestCase):
    def test_integer_descriptor(self):
        data = Data(100, "Test", 50)
        self.assertEqual(data.num, 100)
        with self.assertRaises(TypeError):
            data.num = "invalid"

    def test_string_descriptor(self):
        data = Data(100, "Test", 50)
        self.assertEqual(data.name, "Test")
        with self.assertRaises(TypeError):
            data.name = 123

    def test_positive_integer_descriptor(self):
        data = Data(100, "Test", 50)
        self.assertEqual(data.price, 50)
        with self.assertRaises(ValueError):
            data.price = -10
        with self.assertRaises(TypeError):
            data.price = "invalid"
