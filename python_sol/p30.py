# Project Euler 30
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits

ans = 0

for n in range(2,1000000):
    n_str = str(n)
    sum = 0
    for i in n_str:
        sum += int(i)**5
    if sum == n:
        print(n)
        ans += n

print(ans)
