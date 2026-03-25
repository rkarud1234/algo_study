import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    price = int(input())
    dp = [0] * (price + 1)

    # dp 진행
    dp[0] = 1
    
    for coin in coins:
        for j in range(coin, price+1):
            dp[j] += dp[j-coin]

    print(dp[price])