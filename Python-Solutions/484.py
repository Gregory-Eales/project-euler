import numpy as np

def get_primes(n, primes=[2]):

    if n < primes[-1]:
        return primes

    m = primes[-1]

    while primes[-1] < n:
        m += 1
        is_prime = True
        for prime in primes:
            if m % prime == 0:
                    is_prime =  False
                    break
            if prime > np.sqrt(m):
                break
        if is_prime == True:
            primes.append(m)

    return primes

def is_prime(n, primes):

    if n > primes[-1]:
        primes = get_primes(n, primes)

    if n in primes:
        return True
    else:
        return False

def get_arithmetic_derivitive(n):
    
