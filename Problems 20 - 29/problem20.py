"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""

import time
import math
start = time.time()

sum_of_digits = 0
factorial = math.factorial(100)
lenFact = len(str(factorial))

for i in range(0, lenFact):
    new = str(factorial)
    sum_of_digits += int(new[i])

elapsed = (time.time() - start)
printed = "{} found in {} seconds".format(sum_of_digits, elapsed)
print(printed)
