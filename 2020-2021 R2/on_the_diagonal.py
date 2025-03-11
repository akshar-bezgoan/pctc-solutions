n = int(input())
m = int(input())
grid = []
for i in range(m):
    raw = input()
    raw = raw.replace(' ', ',')
    raw = raw.split(',')
    grid.append([int(i) for i in raw])

biggest = 0
def check_diagonal(i, j):
    big = 0
    point = grid[i][j]
    for x,y in [(1,-1), (1,1), (-1, -1), (-1, 1)]:
        if -1 < i+x < m and -1< j + y < n:
            o = grid[i+x][j+y]
            if point * o > big:
                big = point* o 
        else:
            continue
    return big

for i in range(m):
    for j in range(n):
        curr = check_diagonal(i,j)
        if curr > biggest:
            biggest = curr

print(biggest)