from collections import defaultdict

N = int(input())
node_dict = defaultdict(list)
for _ in range(N):
    edge_info = list(map(int, input().split()))
    now = edge_info[0]
    for i in range(int((len(edge_info)-2) / 2)):
        node_dict[now].append([edge_info[2*i+1],edge_info[2*i+2]])


def bfs(start, node_dict):
    max_node = (start,0)
    cache = node_dict[start]
    visited = {start}

    while cache:
        tcache = []

        for k,v in cache:
            visited.add(k)
            if v > max_node[1]:
                max_node = (k,v)
            
            for tk, tv in node_dict[k]:
                if tk not in visited:
                    tcache.append([tk, v+tv])
        cache = tcache
    
    return max_node

# random node
bound_node, _ = bfs(1, node_dict)

_, answer = bfs(bound_node, node_dict)
print(answer)
