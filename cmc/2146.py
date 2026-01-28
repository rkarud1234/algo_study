from collections import deque
import sys
# sys.stdin = open('2146.txt', 'r')
input = sys.stdin.readline

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
island_id = [[[0,-1] for _ in range(N)] for _ in range(N)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(sy, sx, visited, island_idx):
    q = deque([(sy,sx)])
    visited[sy][sx]=True
    while q:
        y, x = q.popleft()
        island_id[y][x][0] = island_idx
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx] and m[ny][nx]==1:
                visited[ny][nx]=True
                q.append((ny,nx))

# 섬 지도 만들기
visited = [[False for _ in range(N)] for _ in range(N)]
island_idx = 1
for i in range(N):
    for j in range(N):
        if m[i][j]==1 and not visited[i][j]:
            bfs(i,j,visited,island_idx)
            island_idx+=1

# 전체 섬을 넣고 한번에 bfs 돌리기
answers = []
visited = [[False for _ in range(N)] for _ in range(N)]
q = deque([])
for i in range(N):
    for j in range(N):
        if island_id[i][j][0]!=0:
            q.append((i,j,0,island_id[i][j][0]))
            visited[i][j] = True
while q:
    y, x, dist, cur = q.popleft()
    # print(y,x,dist,cur)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<N and 0<=nx<N:
            if island_id[ny][nx][0]==0 and not visited[ny][nx]:
                visited[ny][nx] = True
                island_id[ny][nx][0] = cur
                island_id[ny][nx][1] = dist+1
                q.append((ny,nx,dist+1,cur))
            elif visited[ny][nx] and island_id[ny][nx][1]!=-1 and cur != island_id[ny][nx][0]:
                answers.append(island_id[ny][nx][1] + dist)
# print(len(q))
# print(answers)
print(min(answers) if answers else 0)
# for line in island_id:
#     for i in line:
#         print(i[0], end=' ')
#     print()
# print()
# for line in island_id:
#     for i in line:
#         print("%2d" % i[1], end=' ')
#     print()
# print()