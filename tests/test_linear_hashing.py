import random

from .base import Base
from hashing.linear_hashing import LinearHashing as HashMap

print("-------------------------------------------")
print("Performance of hashmaps with linear probing")

BIG_MAP = HashMap()
for i in random.sample(range(0, 100000), 100000):
    BIG_MAP.put(i, random.randint(1, 21))


class TestSearch(Base):
    def setUp(self):
        super().setUp()
        self.h = HashMap()

    def test_get_10_from_hashmap(self):
        """Search 10 values from hashmap."""
        self.h = BIG_MAP
        for i in random.sample(range(0, 10), 10):
            self.h[i]

    def test_get_1000_from_hashmap(self):
        """Search 1000 values from hashmap."""
        self.h = BIG_MAP
        for i in random.sample(range(0, 1000), 1000):
            self.h[i]

    def test_get_100000_from_hashmap(self):
        """Search 100000 values from hashmap."""
        self.h = BIG_MAP
        for i in random.sample(range(0, 100000), 100000):
            self.h[i]


class TestSet(Base):
    def setUp(self):
        super().setUp()
        self.h = HashMap()

    def test_put_10_into_hashmap(self):
        """Set 10 values in hashmap."""
        self.h = HashMap()
        for i in random.sample(range(0, 10), 10):
            self.h[i, random.randint(1, 21)]

    def test_put_1000_into_hashmap(self):
        """Set 1000 values in hashmap."""
        self.h = HashMap()
        for i in random.sample(range(0, 1000), 1000):
            self.h[i, random.randint(1, 21)]

    def test_put_100000_into_hashmap(self):
        """Set 100000 values in hashmap."""
        self.h = HashMap()
        for i in random.sample(range(0, 100000), 100000):
            self.h[i, random.randint(1, 21)]


class TestRemove(Base):
    def setUp(self):
        super().setUp()
        self.h = HashMap()

    def test_remove_10_from_hashmap(self):
        """Remove 10 values from hashmap."""
        self.h = BIG_MAP
        for i in random.sample(range(0, 10), 10):
            self.h.remove(i)

    def test_remove_1000_from_hashmap(self):
        """Remove 1000 values from hashmap."""
        self.h = BIG_MAP
        for i in random.sample(range(0, 1000), 1000):
            self.h.remove(i)

    def test_remove_100000_from_hashmap(self):
        """Remove 100000 values from hashmap."""
        self.h = BIG_MAP
        for i in random.sample(range(0, 100000), 100000):
            self.h.remove(i)
