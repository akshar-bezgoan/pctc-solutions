blacklist = [(0,0)]
w = int(input())
h = int(input())
ordered = []
initial = []
for i in range(h):
  initial.append(list(input()))
i, j = 0, 0
ordered.append(initial[i][j])
moves = [(0,1), (1,0), (0, -1), (-1, 0)]
'''
r = [i][j] --> [i][j+1]
d = [i][j] --> [i+1][j]
l = [i][j] --> [i][j-1]
u = [i][j] --> [i-1][j]
'''
change = 0
while len(blacklist) < w*h:
  mov = change % 4
  temp = (i + moves[mov][0], j + moves[mov][1])
  if 0 <= temp[0] < h and 0 <= temp[1] < w and temp not in blacklist:
    i += moves[mov][0]
    j += moves[mov][1]
    ordered.append(initial[i][j])
    blacklist.append((i,j))
  else:
    change += 1
units = 0
max = 0
for i in range(len(ordered)):
  if ordered[i] == '.':
    units += 1
  elif units > max_units:
    max_units = units
    units = 0

if units > max_units:
    max_units = units

print(max_units)

