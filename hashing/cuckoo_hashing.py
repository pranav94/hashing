from .hashmap import HashMap


class CuckooHashing(HashMap):
    def __init__(self):
        super().__init__()
        self.H0 = [(None, None) for _ in range(self.capacity)]
        self.H1 = [(None, None) for _ in range(self.capacity)]

    def get(self, key):
        """Returns the value if the key exists in either of the two hashtables."""
        if self.H0[self.h0(key)][0] == key:
            return self.H0[self.h0(key)][1]

        return self.H1[self.h1(key)][1]

    def put(self, key, value):
        """Inserts the value at one hashtable and rearranges + rehashes if required."""
        k, v = key, value
        self.count += 1
        t, c = 0, 0
        while k is not None and c < self.count:
            H, h = self.getHashTableAndFunction(t)
            temp = H[h(k)]
            H[h(k)] = (k, v)
            (k, v) = temp
            t = 1 - t
            if k == key:
                self.count -= 1
            c += 1

        if c >= self.count and k is not None:
            self.rehash()
            self.put(k, v)

        if self.count / self.capacity > self.load_factor:
            self.rehash()

    def remove(self, key):
        """Remove the key from the hashtable in which it exists."""
        if self.H0[self.h0(key)][0] == key or self.H1[self.h1(key)][0] == key:
            self.count -= 1

        if self.H0[self.h0(key)][0] == key:
            self.H0[self.h0(key)] = (None, None)

        if self.H1[self.h1(key)][0] == key:
            self.H1[self.h1(key)] = (None, None)

    def h0(self, key):
        """Hash function used to index H0."""
        return abs(hash(key) % self.capacity)

    def h1(self, key):
        """Hash function used to index H1."""
        return abs((hash(key) // self.capacity) % self.capacity)

    def getHashTableAndFunction(self, t):
        """Returns (h0, H0) if t = 0, returns (h1, H1) if not.
        
        Args:
            t (int): The integert representing the hashtable
                        and hash function to use. (0 or 1)
        
        """
        if t == 0:
            return (self.H0, self.h0)
        return (self.H1, self.h1)

    def rehash(self):
        """Rehash the two hashtables by creating new hashtables double the size."""
        H0 = self.H0
        H1 = self.H1
        self.capacity = 2 * self.capacity
        self.H0 = [(None, None) for _ in range(self.capacity)]
        self.H1 = [(None, None) for _ in range(self.capacity)]

        for k, v in H0:
            if k is not None:
                self[k] = v

        for k, v in H1:
            if k is not None:
                self[k] = v
