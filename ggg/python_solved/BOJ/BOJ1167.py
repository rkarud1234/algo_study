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

# 1. 트리의 루트는 1이라고 가정
# 2. 루트에서 시작해서 탐색하기
visited = [False] * (V+1)
# 자식 노드들중에서 거리가 젤 먼걸 찾아야한다
# 갈라지는 지점에서는 dfs로 max를 비교해야한다.
ans = 0
max_list = [0] * (V+1)
def dfs(curr, curr_dist):
    visited[curr] = True

    # 갈라지는 지점에서 현재 노드로 올 수 있는 최댓값을 탐색한다
    next_dist = [0,0]
    for next in graph[curr]:
        if not visited[next[0]]:
            now_dist = dfs(next[0], next[1])
            if now_dist > next_dist[0]:
                next_dist[1] = next_dist[0]
                next_dist[0] = now_dist
            else:
                next_dist[1] = max(next_dist[1], now_dist)

    # 아닌 경우 - max list만 업데이트
    max_list[curr] = next_dist[0] + curr_dist

    # 갈라지는 지점이 기준이 되는 경우 - ans 업데이트
    next_dist.sort(reverse=True)
    global ans
    ans = max(ans, sum(next_dist), max_list[curr])

    return next_dist[0] + curr_dist

dfs(1,0)
print(ans)
