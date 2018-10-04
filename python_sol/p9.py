# Project Euler # 9
# There exists exactly one Pythagorean triplet (a^2 + b^2 = c^2) for which
# a+b+c = 1000. Find the product abc

# Max value of c is 1000
for b in range(1001):
    a = (1000**2-2000*b)/(2000-2*b)
    print(a)
    c = 1000 - a - b
    if a**2+b**2 == c**2 and int(a)==a and a!=c:
        #checks for pythagorean square, makes sure a is an integer, and that a
        # doesn't equal c
        print("a: {},b: {},c: {}".format(a,b,c))
        print(a*b*c)
        break
