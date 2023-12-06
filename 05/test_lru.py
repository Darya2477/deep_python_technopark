import unittest
from lru import LRUCache


class LRUTest(unittest.TestCase):
    def SetUp(self):
        pass

    def tearDown(self):
        pass

    def test_limit_is_negative(self):
        with self.assertRaises(Exception):
            LRUCache(limit=-1)

    def test_limit_is_zero(self):
        with self.assertRaises(Exception):
            LRUCache(limit=0)

    def test_limit_is_one(self):
        cache = LRUCache(limit=1)
        cache.set("key1", 1)
        cache.set("key2", 2)

        self.assertIsNone(cache.get("key1"))
        self.assertEqual(cache.get("key2"), 2)

    def test_empty_cache(self):
        cache = LRUCache(limit=3)

        self.assertIsNone(cache.get("key1"))
        self.assertIsNone(cache.get("key2"))

    def test_cache_update_existing_key(self):
        cache = LRUCache(limit=3)
        cache.set("key1", 1)
        cache.set("key2", 2)

        cache.set("key2", 20)

        self.assertEqual(cache.get("key1"), 1)
        self.assertEqual(cache.get("key2"), 20)

    def test_cache_set_and_get(self):
        cache = LRUCache(limit=3)
        cache.set("key1", 1)
        cache.set("key2", 2)
        cache.set("key3", 3)

        self.assertEqual(cache.get("key1"), 1)
        self.assertEqual(cache.get("key2"), 2)
        self.assertEqual(cache.get("key3"), 3)
        self.assertIsNone(cache.get("key4"))

    def test_cache_overflow(self):
        cache = LRUCache(limit=2)
        cache.set("key1", 1)
        cache.set("key2", 2)

        cache.set("key3", 3)
        cache.set("key4", 4)

        self.assertIsNone(cache.get("key1"))
        self.assertIsNone(cache.get("key2"))
        self.assertEqual(cache.get("key3"), 3)
        self.assertEqual(cache.get("key4"), 4)

    def test_cache_rearrangement(self):
        cache = LRUCache(limit=3)
        cache.set("key1", 1)
        cache.set("key2", 2)
        cache.set("key3", 3)

        cache.get("key1")
        cache.set("key4", 4)

        self.assertEqual(cache.get("key1"), 1)
        self.assertIsNone(cache.get("key2"))
        self.assertEqual(cache.get("key3"), 3)
        self.assertEqual(cache.get("key4"), 4)

    def test_cache_with_capacity_1(self):
        cache = LRUCache(1)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), "val2")

    def test_change_value_existing_key(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k1", "val1_new")
        cache.set("k3", "val3")

        self.assertEqual(cache.get("k1"), "val1_new")
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), None)


if __name__ == "__main__":
    unittest.main()
