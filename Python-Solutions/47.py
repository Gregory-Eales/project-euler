import numpy as np
import math
from tqdm import tqdm


def get_primes(n):

	primes = [2]

	for i in tqdm(range(3, n), "Getting Primes"):

		is_prime = True

		for p in primes:

			if p > i:
				break

			if i % p == 0:
				is_prime = False
				break
		
		if is_prime:
			primes.append(i)

	return primes


def find_the_four():

	pass

def main():
	print(get_primes(100))


if __name__ == "__main__":
	main()
