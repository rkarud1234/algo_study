import sys
input = sys.stdin.readline

T = int(input())

arr = [1, 2, 3]
dp = [0] * (10001)

# dp 진행
dp[0] = 1

for num in arr:
    for j in range(num, 10001):
        dp[j] += dp[j-num]

for _ in range(T):
    N = int(input())
    print(dp[N])