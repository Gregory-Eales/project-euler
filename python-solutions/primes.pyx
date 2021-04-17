import math
from tqdm import tqdm



cpdef get_primes(int n):

	cdef int i, p
	cdef bint is_prime
	primes = [2]

	for i in tqdm(range(3, n+1), "getting primes"):

		is_prime = True

		for p in primes:

			if p > math.sqrt(i):
				break

			if i%p == 0:
				is_prime = False
				break
		
		if is_prime:
			primes.append(i)
	
	return primes