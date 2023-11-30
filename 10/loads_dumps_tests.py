import unittest
import json
import ujson
import cjson

class TestJsonMethods(unittest.TestCase):

    def test_json_loads(self):
        json_str = '{"hello": 10, "world": "value"}'
        json_doc = json.loads(json_str)
        ujson_doc = ujson.loads(json_str)
        cjson_doc = cjson.loads(json_str)
        self.assertEqual(json_doc, ujson_doc)
        self.assertEqual(json_doc, cjson_doc)

    def test_json_dumps(self):
        json_obj = {"hello": 10, "world": "value"}
        json_str = json.dumps(json_obj)
        ujson_str = ujson.dumps(json_obj)
        cjson_str = cjson.dumps(json_obj)
        self.assertEqual(json_str, ujson_str)
        self.assertEqual(json_str, cjson_str)

if __name__ == '__main__':
    unittest.main()