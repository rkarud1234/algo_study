from collections import deque

N, K = map(int, input().split())

q = deque()

sum = 0
ans = -10000000

for i, val in enumerate(map(int, input().split())):
    q.append(val)
    if i < K:
        sum += val
    else:
        ans = max(ans, sum)
        sum = sum - q.popleft() + val

print(max(ans, sum))

