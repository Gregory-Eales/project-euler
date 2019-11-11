
def self_power(n):
    return n**n

n = 0
for i in range(1, 1001):
    n += self_power(i)



print(str(n)[-10:])
