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

		if n%p == 0:
	
			if p not in factors:
				factors.append(p)

			n = n / p
	
	if n not in factors and n != 1:
		factors.append(int(n))
	
	return factors

def find_the_four(n):

	primes = get_primes(n)

	four_pairs = []

	fours = []

	consecutive = False

	for i in tqdm(range(2, n), "Finding the Four"):
	
		if len(factor(i, primes)) == 4:
			
			if not consecutive:
				consecutive = True

			fours.append(i)

			if len(fours) >= 4:
				four_pairs.append(fours)
				fours = []
		
		elif consecutive:
			fours = []
			consecutive = False
		
	return four_pairs

def main():
	print(find_the_four(150000))
	
	#primes = get_primes(100)
	#print(factor(100, primes))

if __name__ == "__main__":
	main()
