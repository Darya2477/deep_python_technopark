import unittest
from unittest.mock import Mock, patch
import time
from io import StringIO
import re
from deco import mean


class TestMeanDecorator(unittest.TestCase):
    def test_one_call(self) -> None:
        mock = Mock()
        mock = (mean(1))(mock)
        with patch('sys.stdout', new=StringIO()) as out:
            mock()
            printed = out.getvalue()
            self.assertTrue(printed.startswith("Mean execution time for the last 1 calls:"))

    def test_sleep(self) -> None:
        sleep = time.sleep
        sleep = (mean(5))(sleep)
        pattern = r'\d+\.\d+|\d+'
        with patch('sys.stdout', new=StringIO()) as out:
            for _ in range(10):
                sleep(0.1)
                printed = out.getvalue()
                numbers = re.findall(pattern, printed)
                execution_time = float(numbers[-1])
                self.assertAlmostEqual(execution_time, 0.1, delta=1e-2)

    def test_mean_of_zero(self) -> None:
        mock = Mock()
        with self.assertRaises(ValueError) as error:
            mock = (mean(0))(mock)
        self.assertEqual(str(error.exception), "Значение k должно быть положительным")
