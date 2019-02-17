from .hashmap import HashMap


class QuadraticHashing(HashMap):
    def get(self, key):
        """Returns the value for the given key."""
        i = self.h(key)
        count = 0
        while self.H[i].key is not None and self.H[i].key != key:
            count += 1
            i = (i+(count ** 2)) % self.capacity

        return self.H[i].value

    def remove(self, key):
        """
        Removes the node for the key and rearrange
        all the subsequent not None items for further searches.
        """
        i = self.h(key)
        count = 0
        if self.H[i].key is None:
            return
        while self.H[i].key is not None and self.H[i].key != key:
            count += 1
            i = (i + (count ** 2)) % self.capacity

        count += 1
        j = (i+(count ** 2)) % self.capacity

        while self.H[j].key is not None:
            count += 1
            if self.h(self.H[j].key) not in range(i+1, j+1):
                self.H[i].key = self.H[j].key
                self.H[i].value = self.H[j].value
                i = j
            j = (i + (count ** 2)) % self.capacity

        self.count -= 1
        self.H[i].key = None
        self.H[i].value = None

    def put(self, key, value):
        """
        Tries to insert at the hash index. If not empty,
        inserts at the subsequent empty slot. Rehashes if required.
        """
        i = self.h(key)
        count = 0
        while self.H[i].key is not None and self.H[i].key != key:
            count += 1
            i = (i+(count ** 2)) % self.capacity

        if self.H[i].key != key:
            self.count += 1

        self.H[i].key = key
        self.H[i].value = value
        self.rehashIfRequired()
