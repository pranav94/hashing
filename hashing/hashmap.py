from .linked_list import LinkedListNode


class HashMap():
    """Boiler plate for hashmaps. Does not handle collisions."""

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.load_factor = .25
        self.H = [LinkedListNode() for _ in range(self.capacity)]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key, value)

    def put(self, key, value):
        node = self.H[self.h(key)]
        if node.key is None:
            self.count += 1

        node.key = key
        node.value = value

        if self.count / self.capacity > self.load_factor:
            self.rehash()

    def h(self, key):
        return abs(hash(key) % self.capacity)

    def get(self, key):
        node = self.H[self.h(key)]
        if node.key != key:
            return None
        return node.value

    def remove(self, key):
        if self[key] is None:
            return

        self.count -= 1
        self[key] = None

    def rehash(self):
        H = self.H
        self.capacity = 2 * self.capacity
        self.H = [LinkedListNode() for _ in range(self.capacity)]

        for node in H:
            if node.key is not None:
                self[node.key] = node.value

    def getLoadFactor(self):
        return self.count / self.capacity