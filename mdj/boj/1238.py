# 1238. 파티
import heapq
from collections import defaultdict

def dijkstra(graph, start):
    # 1. 모든 노드의 거리를 무한대로 초기화
    distances = {node: float('inf') for node in graph}
    # 2. 시작 노드의 거리는 0으로 설정
    distances[start] = 0
    # 3. (거리, 노드) 형태의 우선순위 큐 생성
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        # 가장 거리가 짧은 노드 정보 꺼내기
        current_distance, current_node = heapq.heappop(queue)

        # 현재 꺼낸 거리가 이미 저장된 거리보다 크면 무시 (최적화)
        if distances[current_node] < current_distance:
            continue
        
        # 인접 노드 확인
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # 더 짧은 경로를 발견한 경우 업데이트
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
                
    return distances


N, M, X = map(int,input().split())

graph = defaultdict(dict)
for _ in range(M):
    s, e, ti = map(int, input().split())
    graph[s-1][e-1] = ti
    

cost_map = {i : dijkstra(graph, i) for i in range(N)}

result = 0
for i in range(N):
    result = max(cost_map[i][X-1] + cost_map[X-1][i], result)

print(result)