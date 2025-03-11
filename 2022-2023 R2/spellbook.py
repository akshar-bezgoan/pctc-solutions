n = int(input())
book = {}
for i in range(n):
    book[i+1] = int(input())


lens = []
cache = {}
for i in range(1, n+1):
    visited = []
    curr = i
    visited.append(curr)
    nx = book[curr]
    spells = 1
    while nx not in visited:
        curr = nx
       

        visited.append(curr)
        nx = book[curr]
        spells += 1
    cache[i] = visited[1:]
    lens.append(spells)

lens = sorted(lens)
freq = 0
for i in lens:
    if i == lens[-1]:
        freq += 1

print(lens[-1])
print(freq)