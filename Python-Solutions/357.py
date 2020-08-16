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


def factor(n, primes):
	
	factors = []
	
	for p in primes:

		if p > int(math.sqrt(n)+1):

			if n in primes:
				factors.append(n)

			break

		if n%p == 0:
	
			if p not in factors:
				factors.append(p)

			n = n / p
	
	if n not in factors and n != 1:
		factors.append(int(n))
	
	return factors


def is_prime(d, n, primes):

	num = d + n/d

	for p in primes:

	


def main():

	get_primes(100,000,000)


if __name__ == "__main__":

	main()
