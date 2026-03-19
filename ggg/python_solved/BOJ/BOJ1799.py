import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def check_valid(i, j, di, dj):
    ni, nj = i, j
    while ni >= 0 and nj >= 0 and ni < N and nj < N:
        if grid[ni][nj] == 2:
            return False
        ni += di
        nj += dj
    return True

def check_valid_full(i, j):
    left_top = check_valid(i, j, -1, -1)
    right_top = check_valid(i, j, -1, 1)
    left_bottom = check_valid(i, j, 1, -1)
    right_bottom = check_valid(i, j, 1, 1)
    return left_top and right_top and left_bottom and right_bottom

def dfs(i, j, cnt):
    if i >= N:
        return cnt
    ans = cnt

    ni = i if j + 2 < N else i+1
    nj = j+2 if j + 2 < N else 1 - (j%2)

    if grid[i][j] == 1 and check_valid_full(i, j):
        grid[i][j] = 2
        ans = max(ans, dfs(ni, nj, cnt+1))
        grid[i][j] = 1
    ans = max(ans, dfs(ni, nj, cnt))
    return ans

print(dfs(0,0,0) + dfs(0,1,0))
