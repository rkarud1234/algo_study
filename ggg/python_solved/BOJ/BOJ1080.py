N, M = map(int, input().split())

A = [list(map(int, input().strip())) for _ in range(N)]
B = [list(map(int, input().strip())) for _ in range(N)]
# 1. 두 행렬에 XOR 연산을 수행한다. -> N*M, 최대 크기 = 50*50 = 2500
xor = [[a ^ b for a, b in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]

# 2. (1)의 결과 행렬을 탐색하면서 1을 발견하면 3*3 칸의 뒤집기를 수행한다. -> N*M = 2500
def flip(si, sj):
    for i in range(si, si+3):
        for j in range(sj, sj+3):
            xor[i][j] ^= 1

ans = 0
for i in range(N):
    for j in range(M):
        if xor[i][j] == 1:
            if i + 2 >= N or j + 2 >= M:
                print(-1)
                exit()
            flip(i,j)
            ans += 1
print(ans)