N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e,t))

import heapq
def dijkstra(start, end):
    dist = [1000001] * (N+1)
    pq = []
    dist[start] = 0
    heapq.heappush(pq, (dist[start], start))

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if dist[curr_node] < curr_dist: # 최단 경로가 아니면 skip
            continue
        for next_node, next_cost in graph[curr_node]:
            if dist[next_node] > curr_dist + next_cost:
                dist[next_node] = curr_dist + next_cost
                heapq.heappush(pq, (dist[next_node], next_node))
    return dist[end]

ans = 0
for i in range(1, N+1):
    if X == i: continue
    ans = max(ans, dijkstra(i,X) + dijkstra(X,i))

print(ans)
