# Evaluate the sum of all the amicable numbers under 10000
# d(n) is the sum of proper divisors of n
# If d(a)=b and d(b)=a then a and b are amicable numbers

def divisor_sum(n): # finds all divisors of n and calculates d(n)
    divisors = [1]
    for i in range(2,round(n**(1/2))):
        if n % i == 0:
            divisors.extend([i,n//i])
    return sum(divisors)


# d = dict() # dictionary is {n:d(n)}
# amicable = set() # ignores duplicates
#
# # sets up dictionary of n:d(n)
# for i in range(10000):
#     if divisor_sum(i) != 1: # ignores prime numbers
#         d[i] = divisor_sum(i)
#
# for i in range(10000):
#     for j in range(10000):
#         try:
#             # finds amicable numbers and ignores cases where n=d(n)
#             if d[i] == j and d[j] == i and d[j] != j and d[i] != i:
#                 amicable.add(i)
#                 amicable.add(j)
#         except KeyError:
#             pass # for prime numbers that aren't keys in d
#     print(i)
#
# print(amicable)
# print(sum(amicable))

# Alternate, more efficient method:
asum = 0
for a in range(2,10000):
    b = divisor_sum(a)
    if b > a:
        if divisor_sum(b) == a:
            asum += a+b

print(asum)
