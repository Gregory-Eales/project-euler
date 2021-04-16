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
	return int(((x**2 - 1)/d))


def get_squares(n):
	return list([i**2 for i in range(1, 100000)])


def find_diaph():

	max_d = 1000
	max_x = 10000
	print(get_y(max_d, max_x))

	squares = get_squares(int(get_y(max_d, max_x)))

	pairs = list([-1e3 for i in range(max_d)])

	for d in tqdm(range(1, max_d)):

		for x in range(2, max_x):

			if (d**0.5 == int(d**0.5)):
				break

			if binary_search(squares, get_y(d, x)):
				
				if x < abs(pairs[d]):
					pairs[d] = x

	
	m_d = 0					
	m_x = 0

	for i in tqdm(range(len(pairs))):

		if m_x < pairs[i]:
			m_x = pairs[i]
			m_d = d


	print(m_d, m_x)



def main():
	find_diaph()

	#print(get_squares(10))


if __name__ == '__main__':
	main()