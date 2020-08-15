import math
import numpy as np
from tqdm import tqdm


def loop(n, k):

	for i in range(n):

		loop(i, k-1)


def brute_combinations(n, k):

	# where n is the maximum number
	# where k is the number of terms

	nums = []

	counter = 0

	
def get_combinations(n, k):

	# where n is the maximum number
	# where k is the number of terms
	

	return n//k


def main():
	target = 100
	ways = [0]*(target+1)
	ways[0] = 1

	for i in range(1, 100):
		for j in range(i, target+1):

			ways[j] += ways[j - i];

	print(ways[-1])

if __name__ == "__main__":

	main()
