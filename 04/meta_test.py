import unittest
from meta import CustomMeta, CustomClass

class CustomClassTests(unittest.TestCase):
    def test_custom_x(self):
        self.assertEqual(CustomClass.custom_x, 50)

    def test_custom_val(self):
        inst = CustomClass()
        self.assertEqual(inst.custom_val, 99)

    def test_custom_line(self):
        inst = CustomClass()
        self.assertEqual(inst.custom_line(), 100)

    def test_str(self):
        inst = CustomClass()
        self.assertEqual(str(inst), "Custom_by_metaclass")

    def test_custom_dynamic(self):
        inst = CustomClass()
        inst.dynamic = "added later"
        self.assertEqual(inst.custom_dynamic, "added later")

    def test_custom_x_error(self):
        inst = CustomClass()
        with self.assertRaises(AttributeError):
            inst.x

    def test_custom_val_error(self):
        inst = CustomClass()
        with self.assertRaises(AttributeError):
            inst.val

    def test_custom_line_error(self):
        inst = CustomClass()
        with self.assertRaises(AttributeError):
            inst.line()

    def test_custom_yyy_error(self):
        inst = CustomClass()
        with self.assertRaises(AttributeError):
            inst.yyy

    def test_custom_dynamic_error(self):
        inst = CustomClass()
        with self.assertRaises(AttributeError):
            inst.dynamic