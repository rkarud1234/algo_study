import sys
input=sys.stdin.readline
from heapq import heapify, heappop, heappush
N, K = map(int, input().split())
jewels, bags = [], []
for _ in range(N):
    jewel = list(map(int, input().split()))
    heappush(jewels, jewel)
for _ in range(K):
    heappush(bags, int(input()))
ans = 0
available = []
while bags and (bag := heappop(bags)):
    # print('bag:', bag)
    while jewels and (jewel := heappop(jewels)):
        [mass, value] = jewel
        if mass <= bag:
            heappush(available, [-value, mass])
        else:
            heappush(jewels, jewel)
            break
    if available:
        [v, m] = heappop(available)
        ans += -v
        # print(v,m)
print(ans)