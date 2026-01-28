n, m = map(int, input().split())

grid = [list(input()) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

finished = False

move = [[1,0], [0,1], [-1,0], [0,-1]]


def is_valid(i, j):
    return i >= 0 and j >= 0 and i < n and j < m


def go(prev, now):
    global finished
    if finished:
        return
    
    visit[now[0]][now[1]] = True

    for d in range(0, 4):
        ni = now[0] + move[d][0]
        nj = now[1] + move[d][1]

        if not is_valid(ni, nj) or grid[now[0]][now[1]] != grid[ni][nj] or (ni == prev[0] and nj == prev[1]):
            continue

        if visit[ni][nj]:
            # 이미 방문한 점을 또 만났다 -> 사이클 
            finished = True
            return
        else:
            # 아닌 경우엔 dfs 진행
            go(now, (ni, nj))


for i in range(0, n):
    for j in range(0, m):
        if visit[i][j]:
            continue
        go((-1, -1), (i, j))

print("Yes" if finished else "No")
