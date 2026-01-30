import sys
# sys.stdin = open('1080.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
# 각 줄은 공백 없이 문자열이므로 split() 없이 읽고, 각 문자를 정수로 변환
before = [list(map(int, list(input().strip()))) for _ in range(N)]
after = [list(map(int, list(input().strip()))) for _ in range(N)]

def is_same(a, b):
    if any(before[i][j]!=after[i][j] for i in range(N) for j in range(M)):
        return False
    else:
        return True

def solve():
    if N<3 or M<3:
        print(-1)
        return
    cnt = 0
    for si in range(N-2):
        for sj in range(M-2):
            # 탈출조건
            if is_same(before, after):
                print(cnt)
                return
            
            # 칸 다를때 3x3뒤집기
            if before[si][sj] != after[si][sj]:
                for i in range(si, si+3):
                    for j in range(sj, sj+3):
                        before[i][j] = 1 - before[i][j]
                cnt+=1
            # 칸 같으면 넘어가기
            else:
                continue
solve()