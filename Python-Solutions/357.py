import numpy as np
import math
from tqdm import tqdm


def prime_test(n):

	start = 2
	end = n

	primes = []
  
	for val in tqdm(range(start, end + 1)): 
		if val > 1:
			for n in range(2, val//2 + 2):
				if (val % n) == 0:
					break
				else:
					if n == val//2 + 1:
						primes.append(val)
	
	return primes

def get_primes(n):

	primes = [2]

	for i in tqdm(range(3, n), "Getting Primes"):

		is_prime = True

		for p in primes:

			if p > int(math.sqrt(i))+5:
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

		if p > num:
			return False

		if p == num:
			return True
	
def main():

	end = 100000

	primes = get_primes(end)

	num = 0
	
	for i in tqdm(range(2, end), "Getting Gen Ints"):

		factors = factor(i, primes)

		prime = True
		
		for f in factors:

			if not is_prime(f, i, primes):

				prime = False

				break
		
		if prime:
			num += i

	print(num)

if __name__ == "__main__":

	main()
