#7/10 testcases passed, 3 time limit exceeded

grid = []
m, n = input().split()
m = int(m)
n = int(n)
for i in range(int(n)):
    grid.append(['.']*int(m))

inx, iny = input().split()
grid[int(iny)][int(inx)] = 'o'

stepx, stepy = input().split()
stepx = int(stepx)
stepy = int(stepy)

moves = int(input())

def move(coord):
    global stepx, stepy
    if coord[0] == 0 or coord[0] == n-1:
        stepy = -stepy
    if coord[1] == 0 or coord[1] == m-1:
        stepx = -stepx
    new = (coord[0] + stepy, coord[1] + stepx)
    return new

curr = (int(iny), int(inx))
for i in range(moves):
    new = move(curr)
    grid[new[0]][new[1]] = 'o'
    grid[curr[0]][curr[1]] = '.'
    curr = new

for i in grid:
    print(''.join(i))
    



"""
[['.', '.', '.', '.', '.'], 
['.', '.', '.', '.', '.'], 
['.', 'o', '.', '.', '.'], 
['.', '.', '.', '.', '.']]


"""
