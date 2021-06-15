"""

The
Fibonacci
sequence is defined
by
the
recurrence
relation:

Fn = Fn−1 + Fn−2, where
F1 = 1 and F2 = 1.
Hence
the
first
12
terms
will
be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The
12
th
term, F12, is the
first
term
to
contain
three
digits.

What is the
index
of
the
first
term in the
Fibonacci
sequence
to
contain
1000
digits?
"""

import time

start = time.time()
Fib = [1, 1]

for i in range(1, 10000000):
    Apples = Fib[i] + Fib[i - 1]
    Fib.append(Apples)
    if Fib[i + 1] >= 10 ** 999:  # I had it at 1000 before but it is 999 since 10 has 2
        break

elapsed = time.time() - start

ans = i + 2  # Breaks at i+1 and then 1 since first index = 0
printed = """ {} found in {} seconds""".format(ans, elapsed)
print(printed)
