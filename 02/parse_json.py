import json

def parse_json(json_str: str, required_fields=None, keywords=None, keyword_callback=None):
    json_doc = json.loads(json_str)
    if required_fields is not None:
        for field in required_fields:
            if field in json_doc:
                value = json_doc[field]
                if keywords is not None:
                    for keyword in keywords:
                        if keyword.lower() in value.lower():
                            if keyword_callback is not None:
                                keyword_callback(keyword, field)
            else:
                print(f"Field {field} not found in JSON")
    else:
        print("No required fields specified")

# Пример использования

def keyword_callback(keyword, field):
    print(f"Keyword '{keyword}' found in field '{field}'")

json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
required_fields = ["key1", "key2"]
keywords = ["word3"]

parse_json(json_str, required_fields, keywords, keyword_callback)
