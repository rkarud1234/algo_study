TC = int(input())

def check_valid(i, j):
    for idx in range(9):
        if idx != j and grid[i][j] == grid[i][idx]:
            return False
        if idx != i and grid[i][j] == grid[idx][j]:
            return False
    # box
    si = (i//3)*3
    sj = (j//3)*3
    for ii in range(si, si+3):
        for jj in range(sj, sj+3):
            if (ii != i or jj != j) and grid[i][j] == grid[ii][jj]:
                return False
    return True


def check_empty(i, j):
    tmp = "123456789"
    for idx in range(9):
        tmp = tmp.replace(grid[i][idx],"") # col
        tmp = tmp.replace(grid[idx][j],"") # row

    # box
    si = (i//3)*3
    sj = (j//3)*3
    for ii in range(si, si+3):
        for jj in range(sj, sj+3):
            tmp = tmp.replace(grid[ii][jj],"")

    return tmp

def dfs(i, j):
    fill = 1
    grid[i][j] = remain[i][j]
    for idx in range(9):
        remain[i][idx] = remain[i][idx].replace(remain[i][j], "")
        if grid[i][idx] == "0" and len(remain[i][idx]) == 1:
            fill += dfs(i, idx)

        remain[idx][j] = remain[idx][j].replace(remain[i][j], "")
        if grid[idx][j] == "0" and len(remain[idx][j]) == 1:
            fill += dfs(idx, j)

    si = (i//3)*3
    sj = (j//3)*3
    for ii in range(si, si+3):
        for jj in range(sj, sj+3):
            remain[ii][jj] = remain[ii][jj].replace(remain[i][j], "")
            if grid[ii][jj] == "0" and len(remain[ii][jj]) == 1:
                fill += dfs(ii, jj)

    return fill

def sudoku():
    for i in range(9):
        for j in range(9):
            if grid[i][j] == "0" and len(remain[i][j]) == 1: # 가능한 숫자가 하나뿐
                return dfs(i, j)
    return 0


for _ in range(TC):
    grid = [list(input().strip()) for _ in range(9)]
    pq = []
    remain = [[""] * 9 for _ in range(9)]

    # 채워야 할 칸 체크
    tot = 0
    for i in range(9):
        if tot < 0:
            break
        for j in range(9):
            if grid[i][j] == "0":
                tot += 1
                remain[i][j] = check_empty(i, j)
            elif not check_valid(i, j):
                tot = -100
    
    while tot > 0:
        filled = sudoku()
        if not filled:
            break
        tot -= filled
    
    if tot == 0:
        for row in grid:
            print("".join(row))
    else:
        print("Could not complete this grid.")
    print()
    
