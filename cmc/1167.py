import sys
input=sys.stdin.readline
V = int(input())
from collections import defaultdict, deque
graph = defaultdict(dict)
for _ in range(V):
    line = list(map(int, input().split()))
    for i in range(1, len(line)-1, 2):
        graph[line[0]][line[i]]=line[i+1]

def bfs(start):
    max_dist=0
    max_node=-1
    visited=[False]*(V+1)
    visited[start]=True
    q=deque([(0, start)])
    while q:
        dist, cur = q.popleft()
        if dist > max_dist:
            max_dist = dist
            max_node = cur

        for nxt, nd in graph[cur].items():
            if not visited[nxt]:
                visited[nxt]=True
                q.append((dist+nd, nxt))
    return max_dist, max_node

d, node = bfs(1)
d, node = bfs(node)
print(d)