from hashing.linear_hashing import LinearHashing
hs = LinearHashing()
hs[15] = 15
hs[31] = 31
hs[47] = 47
hs[15]
hs[31]
hs[47]
hs.remove(31)
hs[31]
hs.remove(15)
hs[15]
hs[47]
hs.remove(47)
hs[47]
hs[15] = 1
hs[15]
[(h.key, h.value) for h in hs.H]

from hashing.quadratic_hashing import QuadraticHashing
hs = QuadraticHashing()
hs[15] = 15
hs[31] = 31
hs[47] = 47
hs[63] = 47
hs.remove(47)
hs[31]
hs.remove(15)
hs[15]
hs[47]
hs.remove(47)
hs[47]
hs[15] = 1
hs[15]
[(h.key, h.value) for h in hs.H]

from hashing.chain_hashing import ChainHashing
hs = ChainHashing()
hs[15] = 15
hs[31] = 31
hs[47] = 47
hs[15]
hs[31]
hs[47]
hs.remove(31)
hs[31]
hs.remove(15)
hs[15]
hs[47]
hs.remove(47)
hs[47]
hs[15] = 1
hs[15]

from hashing.cuckoo_hashing import CuckooHashing
hs = CuckooHashing()
hs[15] = 15
hs[31] = 31
hs[47] = 47
hs[15]
hs[31]
hs[47]
hs.remove(31)
hs[31]
hs.remove(15)
hs[15]
hs[47]
hs.remove(47)
hs[47]
hs[15] = 1
hs[15]

from hashing.hashmap import HashMap
hs = HashMap()
hs.put(15, 0)
hs.get(15)
hs.put(31, 1)
hs.get(31)
hs.put(32, 2)
hs.get(31)
hs.get(32)