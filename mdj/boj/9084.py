import sys
input = sys.stdin.readline

T = int(input())

def solve(n, m, coins):
    dp = [0 for _ in range(m+1)]
    dp[0] = 1
    for coin in coins:
        for i in range(coin, m+1):
            dp[i] += dp[i - coin]

    print(dp[m])

for _ in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    answer = 0
    solve(n,m, coins)

