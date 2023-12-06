
import argparse
import logging

class OptionalFilter(logging.Filter):
    def filter(self, record):
        return "Data retrieval operation" not in record.msg

def apply_log_filter(logger):
    for handler in logger.handlers:
        handler.addFilter(OptionalFilter())
    return logger

class CustomLRUCache:
    class CacheNode:
        def init(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def init(self, capacity=42, log_to_stdout=False, log_filter=False):
        self.__size = 0
        self.capacity = capacity
        self.__cache = {}
        self.__head = None
        self.__tail = None

        self.logger = logging.getLogger("custom_logger")
        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler("cache.log", mode="w")
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter("file: %(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

        if log_to_stdout:
            stdout_handler = logging.StreamHandler()
            stdout_handler.setLevel(logging.INFO)
            stdout_formatter = logging.Formatter("stdout: %(asctime)s - %(levelname)s - %(message)s")
            stdout_handler.setFormatter(stdout_formatter)
            self.logger.addHandler(stdout_handler)

        if log_filter:
            class CustomFilter(logging.Filter):
                def filter(self, record: logging.LogRecord) -> bool:
                    return "limit" in record.getMessage()

            filter = CustomFilter()
            file_handler.addFilter(filter)
            if log_to_stdout:
                stdout_handler.addFilter(filter)

        self.logger.debug("LRUCache is created with capacity = %d", self.capacity)

    def get_value(self, key):
        if key in self.__cache:
            self.logger.info("Data retrieval operation:\tkey %s found in cache", key)
            node = self.__cache[key]
            self.__replace_to_front(node)
            return node.val

        self.logger.warning("Data retrieval operation:\tkey %s not found in cache", key)
        return None

    def set_value(self, key, value):
        if key in self.__cache:
            self.logger.info("Data update operation:\tchanging value for existing key %s to %s", key, value)
            node = self.__cache[key]
            node.val = value
            self.__replace_to_front(node)
        else:
            self.logger.info("Data update operation:\tnew key %s, value %s", key, value)
            if self.__size == self.capacity:
                self.__remove_last()
                self.__size -= 1
            self.__size += 1
            node = self.CacheNode(key, value)
            self.__cache[key] = node
            self.__add_to_front(node)

    def __remove_last(self):
        if self.__tail is None:
            return
        self.logger.info("Data update operation:\tcache overflow, removing last element %s (support)", self.__tail.key)
        del self.cache[self.tail.key]

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
        del self.__tail.next
        self.__tail.next = None

    def __add_to_front(self, node):
        self.logger.debug("Adding a new node to the front %s", node)
        if self.__head is None:
            self.head = self.tail = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node
            
    def __replace_to_front(self, node):
        if self.__head == node:
            self.logger.debug(f"The node %s is already at the front, no need to move", node)
        return
        self.logger.debug("The node %s is not at the front, moving it to the front", node)
        if self.__tail == node:
            self.__tail = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("-s", action="store_true", help="Log to stdout additionally")
        parser.add_argument("-f", action="store_true", help="Apply a custom filter")
        return parser.parse_args()

    def execute_functional_test(cache):
        cache.set_value("k1", "1")
        cache.set_value("k2", "2")
        assert cache.get_value("k3") is None
        assert cache.get_value("k2") == "2"
        assert cache.get_value("k1") == "1"
        cache.set_value("k4", "3")
        cache.set_value("k4", "4")

if name == "main":
args = parse_arguments()

cache = CustomLRUCache(log_to_stdout=args.s, log_filter=args.f)
execute_functional_test(cache)
