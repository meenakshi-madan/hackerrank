#https://www.hackerrank.com/challenges/saveprincess
#!/bin/python
# Head ends here
def displayPathtoPrincess(n,grid):
#print all the moves here
  grid = [list(s) for s in grid]
	for i in range(n):
		if 'm' in grid[i]:
			locm = [i, grid[i].index('m')]
		if 'p' in grid[i]:
			locp = [i, grid[i].index('p')]
	path = []
	while locm[1] < locp[1]:
		path.append('RIGHT')
		locm[1] += 1
	while locm[1] > locp[1]:
		path.append('LEFT')
		locm[1] -= 1
	while locm[0] < locp[0]:
		path.append('DOWN')
		locm[0] += 1
	while locm[0] > locp[0]:
		path.append('UP')
		locm[0] -= 1
	#print n, grid, locm, locp, path
	print '\n'.join(path)

# Tail starts here
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
