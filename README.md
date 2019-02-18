Implementation of the following hashing algorithms in Python with empirical analysis on efficiencies.

1. HashMap without collision handling
2. Linear hashing/Linear Probing
3. Hash Chaining
4. Cuckoo Hashing
5. Quadratic Hashing

Python version: `Python 3.7.0`

To run all the performance tests:
  `make test` or `make`

To run individual performance tests, run any of the following:
1. `python3 -m unittest -q tests/test_linear_hashing.py`
2. `python3 -m unittest -q tests/test_chain_hashing.py`
3. `python3 -m unittest -q tests/test_cuckoo_hashing.py`
4. `python3 -m unittest -q tests/test_quadratic_hashing.py`
