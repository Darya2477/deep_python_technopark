import unittest
from unittest.mock import Mock
from part1 import parse_json


class TestParseJson(unittest.TestCase):
    def test_chislo_in_str(self):
        result = []
        json_str = '{"name": "John", "age": 30, "city": "New York"}'
        required_fields = ["name", "age", "city"]
        keywords = ["John", "New"]

        callback_mock = Mock(side_effect=result.append)

        parse_json(json_str, required_fields, keywords, callback_mock)
        self.assertEqual(result, ["John", "New"])

    def test_not_dict(self):
        result = []
        json_str = "iloveml"
        required_fields = ["i", "love", "ml"]
        keywords = ["machine", "learning"]

        callback_mock = Mock(side_effect=result.append)

        parse_json(json_str, required_fields, keywords, callback_mock)
        self.assertEqual(result, [])

    def test_no_keys(self):
        result = []
        json_str = '{"name": "John", "age": 30, "city": "New York"}'
        required_fields = []
        keywords = ["John", "New"]
        callback_mock = Mock(side_effect=result.append)

        parse_json(json_str, required_fields, keywords, callback_mock)
        self.assertEqual(result, [])

    def test_no_values(self):
        result = []
        json_str = '{"name": "John", "age": 30, "city": "New York"}'
        required_fields = ["name", "age", "city"]
        keywords = []

        callback_mock = Mock(side_effect=result.append)

        parse_json(json_str, required_fields, keywords, callback_mock)
        self.assertEqual(result, [])

    def test_empty_string(self):
        result = []
        json_str = ""
        required_fields = ["name", "age", "city"]
        keywords = []

        callback_mock = Mock(side_effect=result.append)

        parse_json(json_str, required_fields, keywords, callback_mock)
        self.assertEqual(result, [])

    def test_no_coincidences(self):
        result = []
        json_str = '{"name": "John", "age": "30", "city": "New York"}'
        required_fields = ["name", "age", "city"]
        keywords = ["Peter", "34", "Moscow"]

        callback_mock = Mock(side_effect=result.append)

        parse_json(json_str, required_fields, keywords, callback_mock)
        self.assertEqual(result, [])

    def test_one_coincidences(self):
        result = []
        json_str = '{"name": "John", "age": "30", "city": "New York"}'
        required_fields = ["name", "age", "city"]
        keywords = ["John", "98", "Almata"]

        callback_mock = Mock(side_effect=result.append)

        parse_json(json_str, required_fields, keywords, callback_mock)
        self.assertEqual(result, ["John"])

    def test_two_amd_more_coincidences(self):
        result = []
        json_str = '{"name": "John", "age": "30", "city": "New York"}'
        required_fields = ["name", "age", "city"]
        keywords = ["John", "30", "Almata", "New York", "Peter", "34"]

        callback_mock = Mock(side_effect=result.append)

        parse_json(json_str, required_fields, keywords, callback_mock)
        self.assertEqual(result, ["John", "30", "New", "York"])
