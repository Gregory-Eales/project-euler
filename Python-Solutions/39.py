import math
import numpy as np
from tqdm import tqdm as tqdm


def is_traingle(a, b, c):

	if a**2 + b**2 == c**2:
		return True

	else: 
		return False

def get_solutions(n):

	solns = []
	
	for a in range(n):
		for b in range(n):
			for c in range(n):

				if a + b + c == n:
				
					if is_traingle(a, b, c):
						if [a, b, c] not in solns:
							solns.append([a,b,c])

	return len(solns)


def find_max_solutions(p):

	max_p = 0

	for i in tqdm(range(1000), "Getting Max "):

		get_solutions(i)


def main():
	find_max_solutions(100)
	

if __name__ == "__main__":
	main()
