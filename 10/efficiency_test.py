import json
import ujson
from faker import Faker

faker = Faker()

def generate_data(n, size):
    data = []
    for _ in range(n):
        datum = {
            "name": faker.name(),
            "address": faker.address(),
            "phone": faker.phone_number(),
            "email": faker.email(),
        }
        data.append(datum)
    return json.dumps(data).encode("utf-8") * size

def test_json_loads(data):
    for _ in range(1000000):
        json.loads(data)

def test_ujson_loads(data):
    for _ in range(1000000):
        ujson.loads(data)

def test_json_dumps(data):
    for _ in range(1000000):
        json.dumps(data)

def test_ujson_dumps(data):
    for _ in range(1000000):
        ujson.dumps(data)


# Также можно использовать функцию generate_data для генерации данных прямо в коде:

data = generate_data(1000, 10)

test_json_loads(data)
test_ujson_loads(data)

data_obj = json.loads(data)
test_json_dumps(data_obj)
test_ujson_dumps(data_obj)