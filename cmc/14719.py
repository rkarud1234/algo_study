import sys

input = sys.stdin.readline
H, W = map(int, input().split())
h = list(map(int, input().split()))

# 각 칸에 고이는 물 = min(왼쪽 최대, 오른쪽 최대) - 현재 높이 (0 이상)
left_max = [0] * W
right_max = [0] * W

left_max[0] = h[0]
for i in range(1, W):
    left_max[i] = max(left_max[i - 1], h[i])

right_max[W - 1] = h[W - 1]
for i in range(W - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], h[i])

ans = 0
for i in range(W):
    water = min(left_max[i], right_max[i]) - h[i]
    if water > 0:
        ans += water

print(ans)
