# https://www.acmicpc.net/problem/4056
# 0 은 다섯개, 유일한 케이스만 존재

def solve_sdk(board):
    zeros = {}

    def rule_checker(i,j):
        # v check
        vcand = {1,2,3,4,5,6,7,8,9}
        for k in range(9):
            if board[i][k]==0 or (board[i][k] in vcand):
                vcand -= {board[i][k]}
            else:
                return "error"
            
        # h check
        hcand = {1,2,3,4,5,6,7,8,9}
        for k in range(9):
            if board[k][j]==0 or (board[k][j] in hcand):
                hcand -= {board[k][j]}
            else:
                return "error"
        
        # box check
        bcand = {1,2,3,4,5,6,7,8,9}
        bi, bj = i//3, j//3
        for ki in range(3):
            for kj in range(3):    
                kbi = bi * 3 + ki
                kbj = bj * 3 + kj 
                if board[kbi][kbj]==0 or (board[kbi][kbj] in bcand):
                    bcand -= {board[kbi][kbj]}
                else:
                    return "error"
        return vcand.intersection(hcand).intersection(bcand)


    for i in range(9):
        for j in range(9):
            numbers = rule_checker(i,j) 
            if board[i][j] == 0:
                if len(numbers)==0 or numbers=="error":
                    return "Could not complete this grid."
                elif len(numbers)==1:
                    board[i][j] = numbers.pop()
                else:
                    zeros[(i,j)] = numbers
            else:
                if numbers=="error":
                    return "Could not complete this grid."


    # candidate 는 max 2
    while zeros:
        new_zeros = dict()
        # 기존 zero 넣은 경우 체크
        for (zi, zj), cand in zeros.items():
            new_cand = rule_checker(zi, zj)
            if len(new_cand)==0 or new_cand=="error":
                return "Could not complete this grid."
            elif len(new_cand)==1:
                board[zi][zj] = new_cand.pop()
            else:
                new_zeros[(zi,zj)] = new_cand
        zeros = new_zeros


    return "\n".join(["".join(map(str,row)) for row in board])



n = int(input())

for tempt in range(n):
    new_board = []
    for _ in range(9):
        new_board.append(list(map(int, input())))
    print(solve_sdk(new_board))
    print()