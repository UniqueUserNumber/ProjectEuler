/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/


import time
start = time.time()

FirstN = 901
SecondN = 901
Total = 0

for x in range(901,1000):
    for y in range(901,1000):
        Test = x * y
        CharTest = str(Test)
        if CharTest[0] == CharTest[5] and CharTest[1] == CharTest[4] and CharTest[2] == CharTest[3]:
            if Test > Total:
                Total = Test
                FirstN = x
                SecondN = y
                
print("First Number is: " + str(FirstN))
print("Second Number is: " + str(SecondN))



elapsed = (time.time() - start)
Test = "found {} in {} seconds".format(Total,elapsed)
print(Test)
