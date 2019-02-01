import numpy as np
import time

# get primes up to the xth prime
def get_primes(x):
	primes = [2]
	condition = True
	number = 2
	while condition:
		is_prime = True

		if len(primes) == x:
			return primes

		for prime in primes:

			if number % prime == 0:
				is_prime = False

		if is_prime and number not in primes:
			primes.append(number)

		number = number + 1


print(get_primes(10001)[-1])


