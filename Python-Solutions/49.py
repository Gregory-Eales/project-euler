import math
import numpy as np
from tqdm import tqdm
from copy import copy


def get_primes(n):

	primes = [2]

	for i in tqdm(range(3, n), "Getting Primes"):

		is_prime = True

		for p in primes:

			if p > i:
				break

			if i % p == 0:
				is_prime = False
				break
		
		if is_prime:
			primes.append(i)

	return primes


def remove_less_thans(primes, n):

	for i in tqdm(range(len(primes)), "Removing Less Thans"):
		if primes[i] > n:
			primes = primes[i:]
			break

	return primes


def num_to_list(n):
	
	n = str(n)
	l = []
	for i in range(4):
		l.append(int(n[i]))
	
	return l

def list_to_num(l):
		
	n = 0

	for i in range(4):

		n += int(copy(l[i]) * 10**(3-i))
	
	return n

def sort(m):

	l = copy(m)
	
	sorting = True

	while sorting:

		ran = False
		
		for i in range(len(l)-1):

			if l[i] > l[i+1]:
				
				holder = l[i]
				l[i] = l[i+1]
				l[i+1] = holder
				
				ran = True

		if not ran:
			sorting = False

	return l

def get_prime_permutes():
	
	primes = get_primes(10000)
	primes = remove_less_thans(primes, 1000)

	prime_list = []

	pairs = []

	taken = []



	for p in tqdm(primes, "Sorting Digits"):
		
		l = num_to_list(p)
		prime_list.append(copy(l))

	
	for i, p in enumerate(tqdm(prime_list, "Getting Pairs")):
		
		if p in taken:
			pass

		if True:
		
			pair = [p]
			counter = 1
		
			for j, c in enumerate(prime_list):


				#if p == [2, 9, 6, 9] and len(pair) > 1: print(pair)

				if list_to_num(p) == 2969 and len(pair)>1: print(pair)

			
				if i == j:
					pass

				elif sort(p) == sort(c):

										
					if list_to_num(c) - list_to_num(pair[-1]) == 3330 or -1*list_to_num(c) + list_to_num(pair[-1]) == 3330 :
						pair.append(c)
						counter += 1

					if counter == 3 and sort(p) != [1, 4, 7, 9]:

						pairs.append(copy(pair))
								

	return pairs

def main():
	
	pairs = get_prime_permutes()
		
	for p in pairs:
		print(p)

	print(len(pairs))



if __name__ == "__main__":

	main()

	print(num_to_list(5312))

	print(list_to_num([5, 3, 1, 2]))
