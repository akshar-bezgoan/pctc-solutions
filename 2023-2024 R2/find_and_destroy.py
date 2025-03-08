grid = []
for i in range(12):
	grid.append([i for i in input()])
	
coords = {}
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] != '.':
			if grid[i][j] not in coords:
				coords[grid[i][j]] = [(i,j)]
			
			elif (i,j) not in coords[grid[i][j]]:
				coords[grid[i][j]].append((i,j))
		
symbols = list(coords.keys())
i = 0
while len(coords)>1:
	miny, maxy = 13,0
	minx , maxx = coords[symbols[i]][0][0], coords[symbols[i]][-1][0]
	for j in range(len(coords[symbols[i]])):
		if coords[symbols[i]][j][1] < miny:
			miny = coords[symbols[i]][j][1]
		elif coords[symbols[i]][j][1] > maxy:
			maxy = coords[symbols[i]][j][1]
	
	area = (maxy-miny+1) * (maxx-minx+1)
	if len(coords[symbols[i]]) !=  area:
		del coords[symbols[i]]
	i+= 1

sup = list(coords.keys())[0]

for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == sup:
			grid[i][j] = '.'
	print(''.join(grid[i]))



'''
{'#': [(0, 3), (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)],
 '+': [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 4), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4)],
 '@': [(4, 8), (4, 9), (5, 8), (5, 9), (6, 8), (6, 9)],
 '&': [(9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (10, 7), (11, 7)]}

'''
