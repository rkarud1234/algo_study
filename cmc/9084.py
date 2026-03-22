import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M + 1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, M + 1):
            dp[j] += dp[j - coin]
    print(dp[M])
