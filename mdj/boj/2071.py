N = int(input())

go_board_info = [list(map(int, input().split())) for _ in range(4)]

# 바둑판 만들기 미정(-1), 바둑알 없음(0), 바둑알 있음(1)
go_board = [[-1 for _ in range(N)] for _ in range(N)]

# 확정 표시
def draw_info(board, infos):
    # 현재 정보 기반으로 반드시 돌의 유무를 판단 할수 있는 경우에만 체크

    # 현재 정보 기반으로 갱신 할게 있는지 체크
    flag = 0
    # 가로   
    for i in range(N):
        icnt = infos[0][i]
        cnt = {0:0, 1:0}
        unknowns = []
        for j in range(N):
            now = board[i][j]
            if now >= 0:
                cnt[now] += 1
            else:
                unknowns.append((i,j))
            
        if cnt[0] + len(unknowns) == N-icnt:
            for i,j in unknowns:
                board[i][j] = 0
                flag = 1
        elif cnt[1] + len(unknowns) == icnt:
            for i,j in unknowns:
                board[i][j] = 1
                flag = 1

    # 세로
    for j in range(N):
        icnt = infos[1][j]
        cnt = {0:0, 1:0}
        unknowns = []
        for i in range(N):
            now = board[i][j]
            if now >= 0:
                cnt[now] += 1
            else:
                unknowns.append((i,j))
            
        if cnt[0] + len(unknowns) == N-icnt:
            for i,j in unknowns:
                board[i][j] = 0
                flag = 1
        elif cnt[1] + len(unknowns) == icnt:
            for i,j in unknowns:
                board[i][j] = 1
                flag = 1

    # / 대각
    for k in range(2*N-1):
        icnt = infos[2][k]
        cnt = {0:0, 1:0}
        unknowns = []
        ki,kj = min(k,N-1), max(0,k-N+1)
        max_cnt = 0
        for step in range(N):
            i,j = ki-step, kj + step
            if i <0 or j >=N:
                break
            max_cnt += 1
            now = board[i][j]
            if now >= 0:
                cnt[now] += 1
            else:
                unknowns.append((i,j))
            
        if cnt[0] + len(unknowns) == max_cnt-icnt:
            for i,j in unknowns:
                board[i][j] = 0
                flag = 1
        elif cnt[1] + len(unknowns) == icnt:
            for i,j in unknowns:
                board[i][j] = 1
                flag = 1
                
    # \ 대각
    for k in range(2*N-1):
        icnt = infos[3][k]
        cnt = {0:0, 1:0}
        unknowns = []
        ki,kj = max(N-k-1,0), max(0,k-N+1)
        max_cnt = 0

        for step in range(N):
            i,j = ki+step, kj + step
            if i >=N or j >=N:
                break
            max_cnt += 1
            now = board[i][j]
            if now >= 0:
                cnt[now] += 1
            else:
                unknowns.append((i,j))
            
        if cnt[0] + len(unknowns) == max_cnt-icnt:
            for i,j in unknowns:
                board[i][j] = 0
                flag = 1
        elif cnt[1] + len(unknowns) == icnt:
            for i,j in unknowns:
                board[i][j] = 1
                flag = 1
    return flag

def is_right_board(board, infos):
    # 바둑판 정보와 일치하면 True, 모순되면 False, -1 이 존재하면 해당 인덱스 반환하는 함수
    # 가로   
    for i in range(N):
        icnt = infos[0][i]
        cnt = 0
        for j in range(N):
            now = board[i][j]
            if now == -1:
                return (i,j)
            elif now == 1:
                cnt += 1 
        if cnt != icnt:
            return False
        
    # 세로
    for j in range(N):
        icnt = infos[1][j]
        cnt = 0
        for i in range(N):
            now = board[i][j]
            if now ==-1:
                return (i,j)
            elif now == 1:
                cnt += 1
            
        if cnt != icnt:
            return False

    # / 대각
    for k in range(2*N-1):
        icnt = infos[2][k]
        cnt = 0
        ki,kj = min(k,N-1), max(0,k-N+1)
        for step in range(N):
            i,j = ki-step, kj + step
            if i <0 or j >=N:
                break
            now = board[i][j]
            if now == 1:
                cnt += 1
        if cnt != icnt:
            return False
            
    # \ 대각
    for k in range(2*N-1):
        icnt = infos[3][k]
        cnt = 0
        ki,kj = max(N-k-1,0), max(0,k-N+1)

        for step in range(N):
            i,j = ki+step, kj + step
            if i >=N or j >=N:
                break
            now = board[i][j]
            if now == 1:
                cnt += 1
            
        if cnt != icnt:
            return False
    return True


def back_tracking(board):
    new_board = [[x for x in row] for row in board]
    # 현재 보드 상태 기반 갱신 될때 까지 체크
    check_flag = 1
    while check_flag:
        check_flag = draw_info(new_board, go_board_info)

    ret = is_right_board(new_board, go_board_info)
    if ret == True:
        # 재귀 탈출
        return new_board
    elif ret == False:
        # 이전 재귀 복귀
        return False
    else:
        i,j = ret
        new_board[i][j] = 1
        back_ret = back_tracking(new_board)
        if back_ret == False:
            new_board[i][j] = 0
            return back_tracking(new_board)
        else:
            return back_ret


go_board = back_tracking(go_board)


    
# 집 세기
visited = set()
answer = 0
for i in range(1, N-1):
    for j in range(1, N-1):
        if go_board[i][j] == 0 and (i,j) not in visited:
            visited.add((i,j))
            cache = [(i,j)]
            room_size = 1
            is_room = True
            while cache:
                ci, cj = cache.pop()
                # up
                if ci-1==0 and go_board[ci-1][cj]==0:
                    is_room = False

                elif go_board[ci-1][cj]== 0 and (ci-1,cj) not in visited:
                    cache.append((ci-1,cj))
                    visited.add((ci-1,cj))
                    room_size += 1

                # down
                if ci+1==N-1 and go_board[ci+1][cj]==0:
                    is_room = False
                elif go_board[ci+1][cj]==0 and (ci+1,cj) not in visited:
                    cache.append((ci+1,cj))
                    visited.add((ci+1,cj))
                    room_size += 1

                # right
                if cj+1==N-1 and go_board[ci][cj+1]==0:
                    is_room = False
                elif go_board[ci][cj+1]==0 and (ci,cj+1) not in visited:
                    cache.append((ci, cj+1))
                    visited.add((ci, cj+1))
                    room_size += 1

                # left
                if cj-1==0 and go_board[ci][cj-1]==0:
                    is_room = False
                elif go_board[ci][cj-1]==0 and (ci,cj-1) not in visited:
                    cache.append((ci, cj-1))
                    visited.add((ci, cj-1))
                    room_size += 1
            if is_room:
                answer += room_size

print(answer)
