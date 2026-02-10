import sys
input = sys.stdin.readline
l=[]
while (n:=int(input().strip()))!=0:
    l.append(n)

def DP(N):
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    dp[N][0] = 1

    for i in range(N, -1, -1):
        for j in range(N, -1, -1):
            if 0<=i+1<N+1 and 0<=j-1<N+1:
                dp[i][j] += dp[i+1][j-1]
            if 0<=j+1<N+1:
                dp[i][j] += dp[i][j+1]
    print(dp[0][0])
for i in l:
    DP(i)