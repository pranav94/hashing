import random

from hashing.chain_hashing import ChainHashing as HashMap
from tests.base import Base, TestSearch, TestSet, TestRemove

BIG_MAP = HashMap()
for i in random.sample(range(0, 100000), 100000):
    BIG_MAP.put(i, random.randint(1, 21))


class TestHashMapSearch(Base, TestSearch):
    def __init__(self, methodName):
        super().__init__(methodName)
        self.BIG_MAP = BIG_MAP

    def setUp(self):
        super().setUp()
        self.h = HashMap()


class TestHashMapSet(Base, TestSet):
    def setUp(self):
        super().setUp()
        self.h = HashMap()


class TestHashMapRemove(Base, TestRemove):
    def __init__(self, methodName):
        super().__init__(methodName)
        self.BIG_MAP = BIG_MAP

    def setUp(self):
        super().setUp()
        self.h = HashMap()


print("-------------")
print("Hash chaining")
print("-------------")