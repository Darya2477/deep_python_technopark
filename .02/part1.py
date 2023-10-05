import json


def parse_json(
    json_str: str, required_fields=None, keywords=None, keyword_callback=None
):
    try:
        json_doc = json.loads(json_str)
    except json.decoder.JSONDecodeError:
        print("Ошибка при парсинге json:")
    except Exception as ex:
        print("Неизвестная ошибка: ", ex)
    else:
        if (required_fields is not None and keywords is not None) and isinstance(json_doc, dict):
            for key in list(filter(lambda x: x in json_doc.keys(), required_fields)):
                for item in list(
                    filter(
                        lambda x: x in str(json_doc[key]).split(),
                        (" ".join(map(str, keywords))).split(),
                    )
                ):
                    keyword_callback(item)

        return


################################################################################################
# result=[]
# def keyword_callback(keyword):
#     result.append(keyword)

# json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
# required_fields = ["key1"]
# keywords = ["word2"]

# parse_json(json_str, required_fields, keywords, keyword_callback)

# print(result)
