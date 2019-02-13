import time

# number of divisors
def number_divisors(n):
    if n % 2 == 0: n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors

# find the triangle number with factors >= factor limit
def find_triangle_factor(factor_limit):
    n = 1
    lnum, rnum = number_divisors(n), number_divisors(n+1)
    while lnum * rnum < 500:
        n += 1
        lnum, rnum = rnum, number_divisors(n+1)
    return n
 
start = time.time()
index = find_triangle_factor(500)
triangle = (index * (index + 1)) / 2
elapsed = (time.time() - start)
 
print("result {} returned in {} seconds".format(triangle,elapsed))


