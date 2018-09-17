# The "for" loop
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
# using "range" and "xrange".
# "range" returns new list with number of specified range
# "xrange" returns iterator, which is more efficient
# (Python 3 uses the range function, which acts like xrange)
for x in range(5):
    print(x)

for x in range(3, 6):
    print(x)
    
for x in range(3, 8, 2):
    print(x)
    
# The "while" loop
count = 0
while count < 5:
    print(count)
    count += 1
# The "break" and "continue" statements
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)