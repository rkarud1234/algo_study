N, K = map(int, input().split())
A = list(map(int, input().split()))
P = list(map(int, input().split()))
N = len(A)

def dfs(mask, la, ta, p, l):
    global answer, cnt
    # fs = frozenset(v)
    if mask in best:
        if ta >= best[mask]: # total attack값이 크면 바로 탈락
            return
        else:
            best[mask] = ta
    else:
        best[mask] = ta
    #탈출조건
    if ta>K or l>N:
        # print(a, p, l)
        return
    else:
        answer = max(answer, p)
    for i in range(N):
        # if not visited[i]:
        if mask & (1 << i) == 0: # 방문 안한 원소
            # visited[i] = True
            mask |= (1 << i) # 원소 i 추가
            # visits.add(i)
            # print(visited)
            cnt += 1
            dfs(mask, la+A[i], ta+la+A[i], p+P[i], l+1)
            # visited[i] = False
            mask &= ~(1 << i) # 원소 i 제거
            # visits.discard(i)

cnt = 0
answer = 0
visits, last_attack, total_attack, people, level = set([]), 0, 0, 0, 0
# visited = [False for _ in range(N)]

best = {} # pruning을 위한 best 정의
mask = 0 # visit집합을위한 bitmask

dfs(mask, last_attack, total_attack, people, level)
print(answer)
# print(cnt)