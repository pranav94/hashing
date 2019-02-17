import time
import unittest

from hashing.hashmap import HashMap


class Base(unittest.TestCase):
    def setUp(self):
        self._started_at = time.time()
        self.h = HashMap()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        print("-------------------------------------------------")
        print('{},{}'.format(self.shortDescription(), round(elapsed, 4)))
        print("Final load factor,{}".format(self.h.getLoadFactor()))
