import numpy as np
import time

def get_primes(x):
	primes = [2]
	for i in range(2, x):
		number = i
		is_prime = True

		for prime in primes:

			if prime > int(np.sqrt(i)) + 1:
				break

			if number % prime == 0:
				is_prime = False
				break
				
		if is_prime:
			primes.append(number)

	return primes

t = time.time()
primes = get_primes(2000000)
print("Time:", int(time.time() - t), "Seconds")
print(np.sum(primes))