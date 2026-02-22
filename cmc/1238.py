import sys
from collections import deque, defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline
N, M, X = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e,t))

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    dist = [float('inf')]*(N+1)
    dist[start] = 0
    while q:
        curd, cur = heappop(q)
        if curd > dist[cur]:
            continue
        for nxt, nxtd in graph[cur]:
            if dist[nxt] > dist[cur] + nxtd:
                dist[nxt] = dist[cur] + nxtd
                q.append((dist[nxt], nxt))
    return dist
    
results = [dijkstra(i)for i in range(1, N+1)]
print(max(results[i-1][X]+results[X-1][i] for i in range(1, N+1)))