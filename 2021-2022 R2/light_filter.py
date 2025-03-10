w = int(input())
h = int(input())
grid = []
for i in range(h):
    grid.append([int(i) for i in input()])

g1 = []
g2 = []
g3 = []
g4 = []

for i in range(h//2):
    g1.append(grid[i][:w//2])
    g2.append(grid[i][w//2:])

for j in range(h//2, len(grid)):
    g3.append(grid[j][:w//2])
    g4.append(grid[j][w//2:])

count = 0
for i in range(h//2):
    for j in range(w//2):
        if g1[i][j] == g2[i][j] == g3[i][j] == g4[i][j] == 1:
            count += 1


print(count)
