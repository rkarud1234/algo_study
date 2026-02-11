s,N,k,r1,r2,c1,c2 = map(int, input().split())

grid = [[0] * N for _ in range(N)]

start = (N - k) // 2
end = (N + k) // 2
# 초기 N*N 범위는 사전에 초기화
for i in range(start, end):
    for j in range(start, end):
        grid[i][j] = 1

# 탐색 진행
def go(i, j):
    if i<N and j<N:
        return grid[i][j]
    
    if go(i//N, j//N) == 0:
        return go(i%N, j%N)
    else:
        return 1

if s == 0:
    print(0)
else:
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            print(go(i,j), end="")
        print("")
