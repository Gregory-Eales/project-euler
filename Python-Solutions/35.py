import math
import numpy as np
from tqdm import tqdm

def get_primes(n):

	primes = [2]

	for i in tqdm(range(3, n)):
		
		is_prime = True
		for p in primes:

			if p > math.sqrt(i):
				break

			if i % p == 0:
				is_prime = False
				break

		if is_prime:
			primes.append(i)

	return primes

def permute(p):
	
	if len(str(p)) == 1:
		
		return [p]

	permutations = []

	p = str(p)

	for i in range(len(p)-1):
		
		k = p[-1] + p[:-1]

		permutations.append(int(k))

		p = k
	
	return permutations
	
def get_circular_primes(n):
	
	primes = get_primes(n)
	circular_primes = []

	for p in tqdm(primes, "Finding Circulars"):

		is_circ = True
		
		permutations = permute(p)
		
		for perm in permutations:
			
			if perm not in primes:
				is_circ = False
				break

		if is_circ and p not in circular_primes:
			circular_primes.append(p)

	return circular_primes

if __name__ == "__main__":
	
	print(get_primes(1000000)[-1])
	
