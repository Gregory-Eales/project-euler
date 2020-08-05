import math
import numpy as np
from tqdm import tqdm



def get_primes(n):

	primes = [2]

	for i in tqdm(range(3, n), "Getting Primes"):
		
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
	
def get_totient(n, primes):
	return n/len(get_relatives(n, primes))

def get_relatives(n, primes):
	
	relatives = [1]
	
	for i in range(2, n):
		
		is_relative = True
		
		for p in primes:
			
			if p > math.sqrt(i):
				break

			if (n%p == 0) and (i%p==0):
				is_relative = False
				break
			
			"""
			if (n%p != 0) and (i%p!=0):
				is_relative = False
				break
			"""

		if n%i == 0:
			is_relative = False
		
		if is_relative:
			relatives.append(i)
			
	return relatives

def get_max_totient(n):
	
	primes = get_primes(n)

	max_tot = 0

	max_num = 0
	
	for i in tqdm(range(1, n+1), "Getting Max Totient"):
		
		tot = get_totient(i, primes) 
		
		if tot > max_tot:

			max_tot = tot
			max_num = i

	return max_num

if __name__ == "__main__":
	
	"""
	
	primes = get_primes(20)

	print(primes)

	"""

	#print(get_relatives(10, primes))
	
	print(get_max_totient(10000))

	
