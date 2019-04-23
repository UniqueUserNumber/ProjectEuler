/*

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

*/

import time
import math
start = time.time()

Number = 1

for i in range(1,21):
    Number *= i // math.gcd(i,Number)

elapsed = (time.time() - start)
Test = "found {} in {} seconds".format(Number,elapsed)
print(Test)



