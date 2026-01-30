from collections import deque

N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]
group_no = 2
ans = 1000
lands = deque()

move = [[1,0], [0,1], [-1,0], [0,-1]]

def set_group(start):
    global group_no
    q = deque([start])
    lands.append(start)
    grid[start[0]][start[1]] = group_no

    while q:
        cur = q.pop()
        for d in range(0, 4):
            ni = cur[0] + move[d][0]
            nj = cur[1] + move[d][1]

            if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == 1:
                grid[ni][nj] = group_no
                q.append((ni, nj, group_no))
                lands.append((ni, nj, group_no))
    group_no += 1

# 대륙별로 다른 숫자로 그룹화하는 과정
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            set_group((i, j, group_no))


# 최소 거리 구하기
dist = [[0] * N for _ in range(N)]

while lands:
    size = len(lands)
    for s in range(size):
        i, j, group_no = lands.popleft()
        
        for d in range(0, 4):
            ni = i + move[d][0]
            nj = j + move[d][1]

            if 0 <= ni < N and 0 <= nj < N and group_no != grid[ni][nj]: # 같은 육지번호일경우는 체크하지 않는다
                if grid[ni][nj] == 0: # 바다인 경우 계속 진행
                    lands.append((ni, nj, group_no))
                    dist[ni][nj] = dist[i][j] + 1
                    grid[ni][nj] = group_no
                else: # 다른 육지번호를 만난 경우
                    ans = min(ans, dist[i][j] + dist[ni][nj])

print(ans)

