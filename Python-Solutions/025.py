



def get_fib(n):

    fibs = [1, 1]
    for i in range(n-2):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[-1]

def get_m_digit_fib(m):
    fibs = [1, 1]
    while len(str(fibs[-1])) < m:
        fibs.append(fibs[-1] + fibs[-2])
    print(len(fibs))
    return fibs[-1]


print(get_m_digit_fib(1000))
