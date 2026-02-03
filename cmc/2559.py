import sys
# sys.stdin = open('2559.txt', 'r')
input = sys.stdin.readline
N, K = map(int, input().split())
l = list(map(int, input().split()))

ms = s = sum(l[0:K])
for i in range(N-K):
    s = -l[i] + s + l[i+K]
    ms = max(ms, s)

print(ms)
