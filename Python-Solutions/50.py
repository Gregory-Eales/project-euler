import numpy as np
import math
from tqdm import tqdm
import time
from bisect import bisect_left

"""
The prime 41, can be written as the sum of six consecutive primes:

					41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""

def get_primes(n):

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


def binary_search(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    else:
        return False


def sum_cons_primes(primes, i, r):
	return sum(primes[i:i+r])
	

def find_max_consec_sum(primes):

	m = 0
	r = list(reversed(range(1000)))
	primes = list(reversed(primes))
	for j in tqdm(range(len(r)), 'finding sum'):
		for i in range(len(primes)-r[j]):
			s = sum_cons_primes(primes, i, r[j])
			if binary_search(primes, s):
				return s

	return -1		
			

def main():
	
	primes = get_primes(1000000-1)
	print(find_max_consec_sum(primes))
	
	
if __name__ == "__main__":
	main()
