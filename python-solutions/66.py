import math
from tqdm import tqdm
from bisect import bisect_left


def is_diaph(x, y, d):
	return (x**2 - d*(y**2)) == 1


def binary_search(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    else:
        return False


def get_y(d, x):
	return ((x**2 - 1)/d)**0.5


def get_squares(n):
	return list([i**2 for i in range(1, 10000)])


def find_diaph():

	max_d = 1000
	max_x = 10000
	print(get_y(max_d, max_x))

	#squares = get_squares(int(get_y(max_d, max_x)))

	pairs = []

	for d in tqdm(range(1, max_d+1)):

		x = 2
		while True:

			if (d**0.5 == int(d**0.5)):
				break

			if int(get_y(d, x)) == get_y(d, x):
				pairs.append([d, x, get_y(d, x)])
				break

			if x > 1e7:
				break

			x += 1
	
	
	for p in pairs:
		print(p)





def main():
	find_diaph()

	#print(get_squares(10))


if __name__ == '__main__':
	main()