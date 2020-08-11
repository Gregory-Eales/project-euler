import math
import numpy as np
from tqdm import tqdm
import time


def is_traingle(a, b, c):

	if a**2 + b**2 == c**2:
		return True

	else: 
		return False

def get_b(n, a):

	return (n**2 - 2*a*n)/(2*n-2*a)
				
def get_solutions(n):

	solns = []
	
	for a in range(n):
			
			b = get_b(n, a)
	
			if a+b > n or int(b) != b:
				pass

			else:
				c = n - a - b
				if is_traingle(a, b, c):
					if [a, b, c] not in solns:
						solns.append([a,b,c])

	return len(solns)


def find_max_solutions(p):

	max_p = 0
	max_sol = 0

	for i in tqdm(range(p), "Getting Max "):

		poss_sol = get_solutions(i)

		if poss_sol>max_sol:
			max_sol = poss_sol
			max_p = i

	print(max_p)


def main():
	t = time.time()
	find_max_solutions(10000)
	print(round(time.time()-t, 5))
	

if __name__ == "__main__":
	main()
