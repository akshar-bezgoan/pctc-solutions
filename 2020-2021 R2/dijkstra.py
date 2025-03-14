import heapq

def dijkstra(graph, start):
    dist, pred = {start: 0}, {}
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in graph[u]:
            alt = d + w
            if alt < dist.get(v, float('inf')):
                dist[v], pred[v] = alt, u
                heapq.heappush(pq, (alt, v))
    
    return dist, pred

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(dijkstra(graph, 'A'))