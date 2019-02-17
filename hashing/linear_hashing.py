from .hashmap import HashMap


class LinearHashing(HashMap):
    def get(self, key):
        index = self.h(key)
        while self.H[index].key is not None and self.H[index].key != key:
            index = (index+1) % self.capacity

        return self.H[index].value

    def remove(self, key):
        index = self.h(key)
        if self.H[index].key is None:
            return
        while self.H[index].key is not None and self.H[index].key != key:
            index = (index + 1) % self.capacity

        i = index
        j = (index+1) % self.capacity

        while self.H[j].key is not None:
            if self.h(self.H[j].key) not in range(i+1, j+1):
                self.H[i].key = self.H[j].key
                self.H[i].value = self.H[j].value
                i = j
            j = (j+1) % self.capacity

        self.count -= 1
        self.H[i].key = None
        self.H[i].value = None

    def put(self, key, value):
        index = self.h(key)
        while self.H[index].key is not None and self.H[index].key != key:
            index = (index+1) % self.capacity

        if self.H[index].key != key:
            self.count += 1

        self.H[index].key = key
        self.H[index].value = value

        self.rehashIfRequired()