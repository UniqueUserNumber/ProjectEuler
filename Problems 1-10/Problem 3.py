/*

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

*/

import time
start = time.time()

StartValue = 600851475143 

for i in range(2,600851475143):
    if StartValue % i == 0:
        StartValue = StartValue / i
        ans = i
    if StartValue == 1:
        break



elapsed = (time.time() - start)
Test = "found {} in {} seconds".format(ans,elapsed)
print(Test)
