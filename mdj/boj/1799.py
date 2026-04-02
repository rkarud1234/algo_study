# 비숍
 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 10 초	128 MB	36911	9803	6877	25.536%
# 문제
# 서양 장기인 체스에는 대각선 방향으로 움직일 수 있는 비숍(bishop)이 있다. 
# < 그림 1 >과 같은 정사각형 체스판 위에 B라고 표시된 곳에 비숍이 있을 때 비숍은 대각선 방향으로 움직여 O로 표시된 칸에 있는 다른 말을 잡을 수 있다.



# < 그림 1 >

# 그런데 체스판 위에는 비숍이 놓일 수 없는 곳이 있다. < 그림 2 >에서 체스판에 색칠된 부분은 비숍이 놓일 수 없다고 하자. 
# 이와 같은 체스판에 서로가 서로를 잡을 수 없도록 하면서 비숍을 놓는다면 < 그림 3 >과 같이 최대 7개의 비숍을 놓을 수 있다. 색칠된 부분에는 비숍이 놓일 수 없지만 지나갈 수는 있다.



# < 그림 2 >



# < 그림 3 >

# 정사각형 체스판의 한 변에 놓인 칸의 개수를 체스판의 크기라고 한다. 
# 체스판의 크기와 체스판 각 칸에 비숍을 놓을 수 있는지 없는지에 대한 정보가 주어질 때, 서로가 서로를 잡을 수 없는 위치에 놓을 수 있는 비숍의 최대 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 체스판의 크기가 주어진다. 체스판의 크기는 10이하의 자연수이다. 
# 둘째 줄부터 아래의 예와 같이 체스판의 각 칸에 비숍을 놓을 수 있는지 없는지에 대한 정보가 체스판 한 줄 단위로 한 줄씩 주어진다. 
# 비숍을 놓을 수 있는 곳에는 1, 비숍을 놓을 수 없는 곳에는 0이 빈칸을 사이에 두고 주어진다.

# 출력
# 첫째 줄에 주어진 체스판 위에 놓을 수 있는 비숍의 최대 개수를 출력한다.

def diagonals(i, j):
    d_set = set()
    directions = [(1,1),(1,-1),(-1,1), (-1,-1)]
    for di, dj in directions:
        now_i, now_j = i,j
        while now_i >=0 and now_j>=0 and now_i<n and now_j<n:
            d_set.add((now_i, now_j))
            now_i += di
            now_j += dj
    return d_set
            

def dfs(cand,cnt):
    if cand:
        now = cand.pop()
        # 놓은 경우, 안 놓은 경우
        return max(dfs(cand - diagonals_dict[now], cnt+1), dfs(cand, cnt))
    else:
        return cnt


n = int(input())

w_candidate = set()
b_candidate = set()
diagonals_dict = {}
for i in range(n):
    for j, v in enumerate(map(int, input().split())):
        if v:
            if (i+j)%2:
                w_candidate.add((i,j))
            else:
                b_candidate.add((i,j))
            diagonals_dict[(i,j)] = diagonals(i,j)

print(dfs(w_candidate, 0)+ dfs(b_candidate,0))






# 예제 입력 1 
# 5
# 1 1 0 1 1
# 0 1 0 0 0
# 1 0 1 0 1
# 1 0 0 0 0
# 1 0 1 1 1
# 예제 출력 1 
# 7