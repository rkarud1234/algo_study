import sys
input=sys.stdin.readline
dp=[0]*(10001)
dp[0]=1
for j in [1,2,3]:
    for i in range(j, 10001):
        dp[i]+=dp[i-j]
T=int(input())
for _ in range(T):
    n=int(input())
    print(dp[n])