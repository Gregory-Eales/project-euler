import numpy as np
import time
from tqdm import tqdm

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def get_perfect_divisors():
    pass

def is_perfect_number(n):

    divisors = []
    
    for i in range(1, int(n//2) + 1):
        if n%i == 0:
            divisors.append(i)

    if np.sum(divisors) != n:
        return n

    return None

def is_abundant_number(n):

    divisors = []
    
    for i in range(1, int(n//2) + 1):
        if n%i == 0:
            divisors.append(i)

    if np.sum(divisors) > n:
        return n

    return None


def get_non_perfect_numbers(m):
    non_perfect = []
    for i in tqdm(range(m)):
        num = is_perfect_number(i)
        if num != None:
            non_perfect.append(num)
    
    print(non_perfect[0:10])


def get_abundant_numbers(m):
    abundant = []
    for i in tqdm(range(m)):
        num = is_abundant_number(i)
        if num != None:
            abundant.append(num)

    total_sum = m*(m+1)/2

    abundant_sum = np.sum(abundant)
    sum_of_abundants = []
    for i in tqdm(range(len(abundant))):
        for j in range(i, len(abundant)):
            num = abundant[i]+abundant[j]
            if num < m and num not in sum_of_abundants:
                sum_of_abundants.append(num)
    
    print(np.sum(sum_of_abundants))
    print(abundant_sum)
    print(total_sum)
    print("##################")
    print(total_sum - np.sum(sum_of_abundants))


if __name__ == "__main__":

    get_abundant_numbers(28123)
    

