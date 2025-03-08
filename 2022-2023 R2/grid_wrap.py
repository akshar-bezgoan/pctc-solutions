grid = []
for i in range(6):
    grid.append(list(input()))

curr = (0,0)
for i in range(len(grid)):
    if '#' in grid[i]:
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                grid[i][j] = '0'
                curr = (i,j)
                break

visited = [curr]

def next(curr=curr, changes=[(1,0), (0,1), (-1, 0), (0,-1)], grid=grid, visited=visited):
    for x,y in changes:
        newx, newy = curr[0]+x, curr[1]+y
        if newx > 5:
            newx = 0
        elif newx < 0:
            newx = 5
        
        if newy > 5:
            newy = 0
        elif newy < 0:
            newy = 5

        if grid[newx][newy] == '0' and (newx,newy) not in visited:
            curr = (newx, newy)
            visited.append(curr)
            return curr, True
    return curr, False

curr, state = next(curr)
while state == True:
    curr, state = next(curr)


grid[curr[0]][curr[1]] = '#'
for i in grid:
    print(''.join(i))



