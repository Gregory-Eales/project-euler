import math
from tqdm import tqdm


def get_primes(n):
	
	primes = [2]

	for i in tqdm(range(3, n), "Getting Primes"):

			is_prime = True
			for p in primes:

				if p > math.sqrt(i):
					is_prime = True
					break
				
				if i%p == 0:
					is_prime = False
					break
				
			if is_prime:
				primes.append(i)
						
	return primes

# calculate nested root
def get_nested_root(x,y,z):
	return math.sqrt(x + math.sqrt(y) + math.sqrt(z))

def get_unested_root(l):
	num = 0
	for i in l:
		num+=math.sqrt(i)
	return num

# get all non perfect squares
def get_non_squares(n):
	non_squares = []
	for i in tqdm(range(n+1), "Getting Non-Squares"):
		num = math.sqrt(i)
		if num != int(num):
			non_squares.append(i)

	return non_squares


# gets the unested values using the wiki formula (https://en.wikipedia.org/wiki/Nested_radical)
def get_unested(x, y, z):

	s1 = (x + math.sqrt(x**2 - (math.sqrt(y)+math.sqrt(z))) )/2
	s2 = (x - math.sqrt(x**2 - (math.sqrt(y)+math.sqrt(z))) )/2

	s1 = math.sqrt(s1)
	s2 = math.sqrt(s2)

	return s1-s2, s1+s2

# generate possible unested root terms
def generate_number_combinations(n):
	
	nested = generate_nested_roots(n)
	unested = generate_unested_roots(n)

	return nested, unested

# generate possible y and z terms
def generate_nested_roots(n):
	
	# have to be divisble by 4
	# sqrt(y) + sqrt(z) < x

	nested_nums = []
	for i in range(1, n):

		if i < n//9 and int(math.sqrt(i))!= math.sqrt(i):
			nested_nums.append(i)

		elif (i%4 == 0 or i%9 == 0) and int(math.sqrt(i))!= math.sqrt(i):
			nested_nums.append(i)			
	
	return nested_nums			

# generate unested term
def generate_unested_roots(n):

	# have to add up to n
	pass

def generate_hash_table(n):

	root_table = {}

	for i in tqdm(range(n), "Generating Root Table"):
		num = math.sqrt(i)
		if num != int(num):
			root_table[round(num, 5)] = i



	
	
# give the number of denested roots up to n
def f(n):
	
	denested_nums = []

	# get non squares
	#non_squares = get_non_squares(n)
	
	# get primes up to n
	#primes = get_primes(n)

	nested, unested = generate_number_combinations(n)

	table = [False] * int(1e8)


	# check each x for denested roots
	for x in tqdm(range(1, n+1), "Finding De-Nested Roots"):
		
		# can't check every non-square!
		# how to bound the search?

		# each root(z) + root(y) < x
		# sum of unested root terms squared = x
		# get the highest possible number for z and y
	
		"""
		if int(math.sqrt(x-1)) != math.sqrt(x-1):
			denested_nums.append(1 + math.sqrt(x-1))
		"""
	
		
		# case where there are two denested roots
		for i in range(1, x//2 + 1):
		
			num1 = math.sqrt(i) + math.sqrt(x-i)
			num2 = math.sqrt(i*(x-i))

			if int(num2) != num2:
				
				try: table[i**2 + (x-i)**2] = True
				except: pass
		
	
	counter = 0
	for i in tqdm(range(int(1e8)),"Counting Unested Values"):
		if table[i]:
			counter+= 1

	return counter

def test_f():
	print("-"*85)
	r = f(10)
	if r != 17:
		return "Algorithm Failure @ f({}): got {} instead of {}".format(10, r, 17)
	
	r = f(15)
	if r != 46:
		return "Algorithm Failure @ f({}): got {} instead of {}".format(15, r, 46)
	
	r = f(20)
	if r != 86:
		return "Algorithm Failure @ f({}): got {} instead of {}".format(20, r, 86)
	
	"""	
	if f(30) != 213:
		return "Algorithm Failure @ f({})".format(30)
	
	
	if f(100) != 2918:
		return "Algorithm Failure @ f({})".format(100)
	
	
	if f(5000) != 11134074:
		return "Algorithm Failure @ f({})".format(5000)

	"""

	return "Algorithm Success"



if __name__ == "__main__":
	
	#print(test_f())
	
	
	print("-"*85)
	import time
	t = time.time()
	print(f(1200))
	print("it took: {} seconds".format(round(time.time()-t, 5)))
	print("-"*85)
	
	
