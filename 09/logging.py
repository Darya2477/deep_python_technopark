import logging
import argparse

logging.basicConfig(filename='cache.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.INFO)  
console.setFormatter(logging.Formatter('%(asctime)s - %(message)s')) 
logging.getLogger('').addHandler(console)

parser = argparse.ArgumentParser()
parser.add_argument("-s", action="store_true", help="Логировать также в stdout")
parser.add_argument("-f", action="store_true", help="Применить кастомный фильтр")

args = parser.parse_args()

if args.f:
    class CustomFilter(logging.Filter):
        def filter(self, record):
            return len(record.msg.split()) % 2 != 0

    logging.getLogger('').addFilter(CustomFilter())

def main():
    cache = LRUCache() 

    try:
        logging.info("get существующего ключа: %s", cache.get("key1"))

        logging.info("get отсутствующего ключа: %s", cache.get("key100"))

        cache.set("key2", "value2") 

        cache.set("key3", "value3") 

        cache.set("key1", "value1")  

    except Exception as e:
        logging.error("Произошла ошибка: %s", str(e))

if __name__ == "__main__":
    main()
