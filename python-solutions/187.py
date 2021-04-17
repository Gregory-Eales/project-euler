from tqdm import tqdm
import math



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



from primes import get_primes

def main():
	
	primes = get_primes(int(10e6))


if __name__ == '__main__':
	main()