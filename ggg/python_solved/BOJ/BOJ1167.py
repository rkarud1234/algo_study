import sys
sys.setrecursionlimit(10**6)

V = int(input())
graph = dict()

root = 0
for _ in range(V):
    arr = list(map(int, sys.stdin.readline().split()))
    arr.pop()

    graph[arr[0]] = []
    for i in range(1, len(arr), 2):
        graph[arr[0]].append((arr[i], arr[i+1]))

visited = [False] * (V+1)
ans = 0

def dfs(curr, curr_dist):
    visited[curr] = True

    next_dist = [0,0]
    for next in graph[curr]:
        if not visited[next[0]]:
            now_dist = dfs(next[0], next[1])
            if now_dist > next_dist[0]:
                next_dist[1] = next_dist[0]
                next_dist[0] = now_dist
            else:
                next_dist[1] = max(next_dist[1], now_dist)

    global ans
    ans = max(ans, sum(next_dist), next_dist[0] + curr_dist)

    return next_dist[0] + curr_dist

dfs(1,0) # 트리의 루트는 1이라고 가정
print(ans)
