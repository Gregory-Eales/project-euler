import math
from tqdm import tqdm
import time
from bisect import bisect_left

"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any
two primes and concatenating them in any order the result will always
be prime. For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set
of four primes with this property. Find the lowest sum for a set of
five primes for which any two primes concatenate to produce another prime.
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


def concat_is_prime(a, b, primes):
	str_x = str(x)
	str_y = str(y)
	n = int(str_x+str_y)
	return binary_search(primes, n)



def main():
	primes = get_primes(1000)


if __name__ == '__main__':
	main()