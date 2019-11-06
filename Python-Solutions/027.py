
def get_primes(n, primes=[2]):

    if n < len(primes):
        return primes

    m = primes[-1]

    while len(primes) < n:
        m += 1
        is_prime = True
        for prime in primes:
            if m % prime == 0:
                    is_prime =  False
                    break
        if is_prime == True:
            primes.append(m)

    return primes


def polynomial(a, b, n):
    return n**2 + a*n + b

def highest_consecutive_primes(a_max, b_max):

    primes = get_primes(10000)

    max_consecutive = 0
    max_coeff = [0, 0]

    for a in range(a_max):
        for b in range(b_max):
            n = 0
            consecutive = True
            while consecutive == True:
                p = polynomial(a, b, n)
                if p in primes:
                    n += 1
                else:
                    consecutive = False
            if n > max_consecutive:
                max_consecutive = n
                max_coeff = [a, b]

    return max_consecutive, max_coeff

print(highest_consecutive_primes(10, 43))
