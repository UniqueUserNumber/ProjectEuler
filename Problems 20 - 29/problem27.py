
import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


n = 0
primes = []
max_n = 1

for x in range(2, 1000):
    if is_prime(x):
        primes.append(x)

for y in primes:
    for a in range(-1000, 1000):
        SetRange = True
        na = 0
        while SetRange:

            testPrime = na ** 2 + a * na + y
            if is_prime(testPrime):
                n += 1
            else:
                SetRange = False
        if na > max_n:
            maxA = a
            maxB = b
            maxn = na

print(maxA)
print(maxB)
print(maxn)

