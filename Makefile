main test :
		@python3 -m unittest -q tests/test_linear_hashing.py
		@python3 -m unittest -q tests/test_chain_hashing.py
		@python3 -m unittest -q tests/test_cuckoo_hashing.py
		@python3 -m unittest -q tests/test_quadratic_hashing.py
