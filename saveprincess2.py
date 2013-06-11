#!/bin/python
# Head ends here
def nextMove(n,x,y,grid):
  grid = [list(s) for s in grid]
	locm = [x, y]
	for i in range(n):
		#if 'm' in grid[i]:
			#locm = [i, grid[i].index('m')]
		if 'p' in grid[i]:
			locp = [i, grid[i].index('p')]
	path = []
	while locm[1] < locp[1]:
		#path.append('RIGHT')
		#locm[1] += 1
		return 'RIGHT'
	while locm[1] > locp[1]:
		#path.append('LEFT')
		#locm[1] -= 1
		return "LEFT"
	while locm[0] < locp[0]:
		#path.append('DOWN')
		#locm[0] += 1
		return "DOWN"
	while locm[0] > locp[0]:
		#path.append('UP')
		#locm[0] -= 1
		return "UP"
	#print n, grid, locm, locp, path
	#print '\n'.join(path)
	#return ""
# Tail starts here
n = input()
x,y = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,x,y,grid)
