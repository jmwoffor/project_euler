# Project Euler 28
# Starting with the number 1 and moving right in a clockwise direction, what
# is the sum of the numbers on the diagonals in a 1001 by 1001 spiral?

import numpy as np
import math

n = 1001 # size of spiral
spiral = np.zeros((n,n))

mid = math.floor(n/2)
spiral[mid,mid] = 1

col = mid
row = mid
step = 1
rd = 1 # right down direction

while 0 in spiral:
    try:
        if rd == 1: # move to the right, then down
            for r in range(1,step+1):
                spiral[row,col+1] = spiral[row,col] + 1
                col += 1
                #print(spiral)

            for d in range(1,step+1):
                spiral[row+1,col] = spiral[row,col] + 1
                row += 1
                #print(spiral)

            step += 1
            rd = 0

        elif rd == 0: # move to the left, then up
            for l in range(1,step+1):
                spiral[row,col-1] = spiral[row,col] + 1
                col -= 1
            for u in range(1,step+1):
                spiral[row-1,col] = spiral[row,col] + 1
                row -= 1
            step += 1
            rd = 1
        #print(spiral)

    except IndexError:
        break
print(spiral)

dsum = 0
for i in range(n):
    dsum += spiral[i,i]
    dsum += spiral[i,n-1-i]

dsum -= 1 # the loop above double-counts the middle value (always 1)
print(dsum)
