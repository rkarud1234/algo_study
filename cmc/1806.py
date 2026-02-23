import sys
input = sys.stdin.readline
N, S = map(int, input().split())
l = list(map(int, input().split()))
s, e = 0, 0
answer = 1 if l[0]>=S else float('inf')
cur = l[0]
while True:
    if cur>=S:
        answer = min(answer, e-s+1)
        if s<e:
            cur -= l[s]
            s += 1
        elif s==e: break # 길이 1로 최소, 더 볼 필요 없음
    else:
        e += 1
        if e==N: break
        cur += l[e]
print(0 if answer==float('inf') else answer)