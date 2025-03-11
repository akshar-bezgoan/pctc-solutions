'''w = input()
n = int(input())

def shift(w, n):
    if len(w) != 2:
        new = w[n:] + w[:n]
    else:
        if n % 2 ==0:
            return w
        else:
            return w[1] + w[0]
    return new

anagram = ''
while len(w) != 0:
    w = shift(w, n)
    anagram += w[0]
    w = w[1:]

print(anagram)'''

"""n = int(input())
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

print(biggest)"""
    
"""
[[7, 3, 7, 4], 
[2, 8, 1, 6], 
[9, 3, 9, 2], 
[11, 4, 0, 6], 
[2, 2, 1, 15]]
"""


"""n = int(input())
coords = {}
grid = [['.']*10]*10
for i in range(n):
    raw = input()
    raw = raw.replace(' ', ',').split(',')
    x = int(raw[0]) + 10
    y = 10 - int(raw[1])
    symbol = raw[2]
    coords[symbol] = (y, x)
    grid[coords[symbol][0]][coords[symbol][1]] = symbol

print(grid)"""


w = list(input())
n = int(input())
res = ""

while w:
  for _ in range(n):
    w.append(w.pop(0))
  res += w.pop(0)

print(res)