import sys
# sys.stdin = open('16929.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
l = [list(input().strip()) for _ in range(N)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(sy, sx):
    stack = [(sy,sx,-1,-1)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[sy][sx] = True
    while stack:
        y, x, py, px = stack.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M  and l[ny][nx]==l[y][x]:
                if not visited[ny][nx]:
                    visited[ny][nx]=True
                    stack.append((ny,nx,y,x))
                else:
                    if not (ny==py and nx==px):
                        return True

if any(dfs(i,j) for i in range(N) for j in range(M)):
    print('Yes')
else:
    print('No')
    