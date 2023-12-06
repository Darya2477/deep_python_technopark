import unittest
from unittest.mock import MagicMock
from model import SomeModel, predict_message_mood

model = SomeModel()


class TestModel(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_model_less_than_good_trashhold(self):
        self.assertGreater(model.predict("Чапаев и пустота"), 0.8)

    def test_model_more_than_bad_trashhold(self):
        self.assertLess(model.predict("Вулкан"), 0.3)

    def test_model_between_bad_and_good_trashholds(self):
        self.assertGreater(model.predict("Остров сокровищ"), 0.3)
        self.assertLess(model.predict("Остров сокровищ"), 0.8)

    def test_model_more_than_one(self):
        self.assertEqual(model.predict("Алиса в стране чудес"), 0.999999999)

    def test_model_empty_message(self):
        self.assertEqual(model.predict(""), 0)


class TestPredictMessage(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_predict_bad(self):
        self.assertEqual(predict_message_mood("Вулкан", model), "неуд")

    def test_predict_norm(self):
        self.assertEqual(predict_message_mood("Остров сокровищ", model), "норм")

    def test_predict_good(self):
        self.assertEqual(predict_message_mood("Чапаев и пустота", model), "отл")


class TestSomeModel(unittest.TestCase):
    def test_predict_returns_float(self):
        model = SomeModel()
        result = model.predict("test")
        self.assertIsInstance(result, float)

    def test_predict_returns_value_less_than_one(self):
        model = SomeModel()
        result = model.predict("test")
        self.assertLessEqual(result, 0.999999999)

    def test_predict_returns_correct_value(self):
        model = SomeModel()
        result = model.predict("test")
        expected = (116 + 101 + 115 + 116) * len("test") ** 2 / 1114111 * 0.25
        self.assertEqual(result, expected)

    def test_predict_message_mood_returns_neud(self):
        model = MagicMock()
        model.predict.return_value = 0.2
        result = predict_message_mood("test", model)
        self.assertEqual(result, "неуд")

    def test_predict_message_mood_returns_otl(self):
        model = MagicMock()
        model.predict.return_value = 0.9
        result = predict_message_mood("test", model)
        self.assertEqual(result, "отл")

    def test_predict_message_mood_returns_norm(self):
        model = MagicMock()
        model.predict.return_value = 0.5
        result = predict_message_mood("test", model)
        self.assertEqual(result, "норм")

    def test_predict_message_mood_uses_bad_thresholds_default(self):
        model = MagicMock()
        model.predict.return_value = 0.2
        predict_message_mood("test", model)
        model.predict.assert_called_with("test")

    def test_predict_message_mood_uses_good_thresholds_default(self):
        model = MagicMock()
        model.predict.return_value = 0.9
        predict_message_mood("test", model)
        model.predict.assert_called_with("test")

    def test_predict_message_mood_uses_custom_bad_thresholds(self):
        model = MagicMock()
        model.predict.return_value = 0.2
        predict_message_mood("test", model, bad_thresholds=0.5)
        model.predict.assert_called_with("test")

    def test_predict_message_mood_uses_custom_good_thresholds(self):
        model = MagicMock()
        model.predict.return_value = 0.9
        predict_message_mood("test", model, good_thresholds=0.7)
        model.predict.assert_called_with("test")


if __name__ == "__main__":
    unittest.main()
