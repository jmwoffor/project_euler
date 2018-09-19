# Project Euler 15
# Starting at the top left corner of a 20x20 grid, how many routes are there to
# the bottom right corner if you can only move to the left or right?

# Going to use Catalan numbers to solve this. Each node has a Catalan number that
# represents the total possible paths that can be taken to reach that node

import numpy as np
n = 20 # grid size
# in a nxn grid, there are n+1 x n+1 nodes
grid = np.zeros((n+1,n+1), dtype=int)
# Since you can only move in two directions, the top row and left column only have
# one possible path
for i in range(n+1):
    grid[0,i] = 1
    grid[i,0] = 1

# Other nodes have to add the Catalan numbers of the node above and the node to the left
for j in range(1,n+1):
    for i in range(1,n+1):
        grid[i,j] = grid[i-1,j] + grid[i,j-1]

#np.savetxt("p15_grid.csv", grid, fmt='%.0f', delimiter=",") # to make troubleshooting easier
print(grid[n,n])
