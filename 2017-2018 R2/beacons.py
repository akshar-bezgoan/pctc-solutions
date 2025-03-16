from collections import defaultdict, deque
from math import sqrt

graph = defaultdict(list)
graph[(0, 0)] = [] 
maxd = int(input())
n = int(input())  
coords = [(0, 0)]   

def calc_distance(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    d = sqrt(dx**2 + dy**2)
    return d

for i in range(n):
    x, y = map(int, input().split())
    coords.append((x, y))

for i in range(len(coords)):
    x, y = coords[i][0], coords[i][1]
    for j in range(i + 1, len(coords)): 
        x2, y2 = coords[j][0], coords[j][1]
        d = calc_distance(x, y, x2, y2)
        if d <= maxd:
            graph[(x, y)].append((x2, y2))
            graph[(x2, y2)].append((x, y))

def bfs(graph):
    seen = set()
    seen.add((0, 0)) 
    q = deque([(0, 0)])  
    lit_per_minute = [] 
    
    while q:

        level_size = len(q)
        lit_this_minute = 0  

        for _ in range(level_size):
            curr = q.popleft()
            for neighbor in graph[curr]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append(neighbor)
                    lit_this_minute += 1
        
        if lit_this_minute > 0:
            lit_per_minute.append(lit_this_minute)
        else:
            break  
    
    return lit_per_minute

lit_per_minute = bfs(graph)

sum = 0
for beacons_lit in lit_per_minute:
    sum += beacons_lit
    print(sum)