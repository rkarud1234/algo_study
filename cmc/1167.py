import sys
input=sys.stdin.readline
V = int(input())
from collections import defaultdict
graph = defaultdict(dict)
for v in range(V):
    line = list(map(int, input().split()))
    for i in range(1, len(line)-1, 2):
        graph[v+1][line[i]]=line[i+1]
        print(line[i], line[i+1])

for i in graph.items():
    print(i)