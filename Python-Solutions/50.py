import numpy as np
import math
from tqdm import tqdm
import time



def get_primes(n):

	primes = [2]

	for i in tqdm(range(3, n+1), "Getting Primes"):

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


def sum_consecutive_primes():

	pass

def main():
	
	for i in range(1000000):
		pass

	primes = get_primes(1000000)
	print(len(primes))
	
	
if __name__ == "__main__":
	main()
