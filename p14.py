# Project Euler #14
# if n is even: n -> n/2
# elif n is odd: n -> 3n+1
# What starting number under one million produces the longest in the above sequence?

counter_max = 1
max_start = 1

for i in range(2,1000000):
    n = i
    counter = 1
    while n > 1:
        if n % 2 == 0:
            n /= 2
            counter += 1
        else:
            n = 3*n + 1
            counter += 1
    if counter > counter_max:
        counter_max = counter
        max_start = i
    print(i)
print(max_start)
