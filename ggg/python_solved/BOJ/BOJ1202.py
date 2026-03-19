import heapq
import sys
input = sys.stdin.readline

N,K = map(int, input().split())
gems, bags = [], []

for _ in range(N):
    m, v = map(int, input().split())
    # 1순위: 가격 내림차순, 2순위: 무게 오름차순
    heapq.heappush(gems, (m, -v))

for _ in range(K):
    bags.append(int(input()))
bags.sort()

ans = 0
candidate = []
idx = 0

for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(candidate, heapq.heappop(gems)[1])
    if candidate:
        now = -heapq.heappop(candidate)
        ans += now

print(ans)
