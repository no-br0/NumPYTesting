import numpy as np

#grid1 = np.arange(9)
#grid2 = np.split(grid1,3)
#print(grid1)
#print(grid2)
#for i in grid2:
#    print(i)


#print(grid2[0:3])
#print(grid2[::1])
#print(grid2[0::])
#print(grid2[0::])
#print(grid2[1,1])


GRID_SIZE = [3,3]

grid = np.zeros(GRID_SIZE, dtype=int)
#print("Initial Grid")
#print(grid)

grid[0,1] = 1
grid[1,1] = 2
grid[1,0] = 1
grid[2,2] = 3
grid[2,0] = 2
grid[1:3, 1:3] = 1


#print("\nUpdated Grid")
print(grid)

#print(np.sum(grid[0]))
#print(np.sum(grid[1]))
#print(np.sum(grid[1, 1:3]))

#for x in grid[1, 0:3]:
#    print("grid:",x)
#print(np.sum(grid[2]))


