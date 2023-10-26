class LRUCache:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, limit=42):
        self.limit = limit
        self.cache = {}
        self.head = self.Node(None, None)
        self.tail = self.Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)  
            return node.value
        return None

    def set(self, key, value):
        if (self.limit>=1):
            if key in self.cache:
                node = self.cache[key]
                node.value = value
                self._move_to_front(node) 
            else:
                if len(self.cache) >= self.limit:
                    self._evict_last() 
                new_node = self.Node(key, value)
                self._add_to_front(new_node) 
                self.cache[key] = new_node
        else:
            raise Exception('Limit must be greater than or equal to 1.')

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_to_front(node)
    
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _evict_last(self):
        last_node = self.tail.prev
        del self.cache[last_node.key]
        self._remove_node(last_node)


cache = LRUCache(2)

cache.set("k1", "val1")
cache.set("k2", "val2")

assert cache.get("k3") is None
assert cache.get("k2") == "val2"
assert cache.get("k1") == "val1"

cache.set("k3", "val3")

assert cache.get("k3") == "val3"
assert cache.get("k2") is None
assert cache.get("k1") == "val1"
