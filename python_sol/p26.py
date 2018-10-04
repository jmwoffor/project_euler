# Project Euler 26
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle
# in its decimal fraction part

def find_repeat(d):
    x = str(1/d)
    a = 0
    for i in range(2,len(x)): # ignore 0.
        if x[2:2+a] == x[]
