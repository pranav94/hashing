import time
import unittest
import random

from hashing.hashmap import HashMap


class Base(unittest.TestCase):
    def setUp(self):
        self._started_at = time.time()
        self.h = HashMap()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        operation, values = self.shortDescription().split(",")
        print('Operation: {operation: <6} \t# of Values: {} \tTime taken: {}(ms)'.format(values, round(1000*elapsed, 4), operation=operation))


class TestSearch():
    def __init__(self):
        self.BIG_MAP = HashMap()

    def test_get_10_from_hashmap(self):
        """Search,10"""
        self.h = self.BIG_MAP
        for i in random.sample(range(0, 10), 10):
            self.h[i]

    def test_get_100_from_hashmap(self):
        """Search,100"""
        self.h = self.BIG_MAP
        for i in random.sample(range(0, 100), 100):
            self.h[i]

    def test_get_1000_from_hashmap(self):
        """Search,1000"""
        self.h = self.BIG_MAP
        for i in random.sample(range(0, 1000), 1000):
            self.h[i]

    def test_get_10000_from_hashmap(self):
        """Search,10000"""
        self.h = self.BIG_MAP
        for i in random.sample(range(0, 10000), 10000):
            self.h[i]

    def test_get_100000_from_hashmap(self):
        """Search,100000"""
        self.h = self.BIG_MAP
        for i in random.sample(range(0, 100000), 100000):
            self.h[i]


class TestSet():
    def __init__(self):
        self.h = HashMap()

    def test_put_10_into_hashmap(self):
        """Set,10"""
        for i in random.sample(range(0, 10), 10):
            self.h[i, random.randint(1, 21)]

    def test_put_100_into_hashmap(self):
        """Set,100"""
        for i in random.sample(range(0, 100), 100):
            self.h[i, random.randint(1, 21)]

    def test_put_1000_into_hashmap(self):
        """Set,1000"""
        for i in random.sample(range(0, 1000), 1000):
            self.h[i, random.randint(1, 21)]

    def test_put_10000_into_hashmap(self):
        """Set,10000"""
        for i in random.sample(range(0, 10000), 10000):
            self.h[i, random.randint(1, 21)]

    def test_put_100000_into_hashmap(self):
        """Set,100000"""
        for i in random.sample(range(0, 1000000), 100000):
            self.h[i, random.randint(1, 21)]


class TestRemove():
    def __init__(self):
        self.BIG_MAP = HashMap()

    def test_remove_10_from_hashmap(self):
        """Remove,10"""
        self.h = self.BIG_MAP
        for i in random.sample(range(0, 10), 10):
            self.h.remove(i)

    def test_remove_100_from_hashmap(self):
        """Remove,100"""
        self.h = self.BIG_MAP
        for i in random.sample(range(0, 100), 100):
            self.h.remove(i)

    def test_remove_1000_from_hashmap(self):
        """Remove,1000"""
        self.h = self.BIG_MAP
        for i in random.sample(range(0, 1000), 1000):
            self.h.remove(i)

    def test_remove_10000_from_hashmap(self):
        """Remove,10000"""
        self.h = self.BIG_MAP
        for i in random.sample(range(0, 10000), 10000):
            self.h.remove(i)

    def test_remove_100000_from_hashmap(self):
        """Remove,100000"""
        self.h = self.BIG_MAP
        for i in random.sample(range(0, 100000), 100000):
            self.h.remove(i)
