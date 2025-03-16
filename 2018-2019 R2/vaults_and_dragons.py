import heapq
from collections import defaultdict

def addEdge(adj, u, v, wt1, wt2):
    adj[u].append((v, wt1))
    adj[v].append((u, wt2))


def dijkstra(adj, V, src):
    pq = []
    dist = [float('inf')] * V
    srcd = weight(vdata[0])
    heapq.heappush(pq, (srcd,src))
    dist[src] = srcd

    while pq:
        distance, u = heapq.heappop(pq)

        for v, wt in adj[u]:
            if dist[v] > dist[u] + wt:
                dist[v] = dist[u] + wt
                heapq.heappush(pq, (dist[v], v))

    return dist

def weight(state):
    if state == 'D':
        return 1
    else:
        return 0


adj = defaultdict(list)
V = int(input())
vdata = input()
conns = int(input())
for i in range(conns):
    u, v = input().split()
    u,v = int(u)-1, int(v)-1
    wt1 = weight(vdata[v]) #weight going there
    wt2 = weight(vdata[u]) #weight coming back
    addEdge(adj, u, v, wt1, wt2)

treasure = [i for i in range(len(vdata)) if vdata[i] =='T']

print(dijkstra(adj, V, 0)[treasure[0]])

"""
8
DDEDDDTD
13
1 2
1 4
2 3
3 4
2 4
3 8
3 5
4 5
4 6
5 6
6 7
5 7
8 7

"""