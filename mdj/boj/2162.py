# 선분 그룹
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	20908	6847	4830	31.089%
# 문제
# N개의 선분들이 2차원 평면상에 주어져 있다. 선분은 양 끝점의 x, y 좌표로 표현이 된다.

# 두 선분이 서로 만나는 경우에, 두 선분은 같은 그룹에 속한다고 정의하며, 그룹의 크기는 그 그룹에 속한 선분의 개수로 정의한다. 
# 두 선분이 만난다는 것은 선분의 끝점을 스치듯이 만나는 경우도 포함하는 것으로 한다.

# N개의 선분들이 주어졌을 때, 이 선분들은 총 몇 개의 그룹으로 되어 있을까? 
# 또, 가장 크기가 큰 그룹에 속한 선분의 개수는 몇 개일까? 이 두 가지를 구하는 프로그램을 작성해 보자.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 3,000)이 주어진다. 둘째 줄부터 N+1번째 줄에는 양 끝점의 좌표가 x1, y1, x2, y2의 순서로 주어진다. 
# 각 좌표의 절댓값은 5,000을 넘지 않으며, 입력되는 좌표 사이에는 빈칸이 하나 있다.

# 출력
# 첫째 줄에 그룹의 수를, 둘째 줄에 가장 크기가 큰 그룹에 속한 선분의 개수를 출력한다.
from collections import Counter

N = int(input())

points = [list(map(int, input().split())) for _ in range(N)]

def get_func(x1, y1, x2, y2):
    if x1 == x2:
        return "X", x1
    a = (y1 - y2) / (x1 - x2)
    b = y1 - a*x1
    print(a,b)
    return a, b

def check(cross_point, points):

    cx, cy = cross_point
    x1, y1, x2, y2 = points

    lx, hx = min(x1,x2), max(x1,x2)
    ly, hy = min(y1,y2), max(y1,y2)

    return (lx <= cx <= hx) and (ly <= cy <= hy)

def check2(point0, point1):
    x1, y1, x2, y2 = point0
    lx0, hx0 = min(x1,x2), max(x1,x2)
    ly0, hy0 = min(y1,y2), max(y1,y2)
    x1, y1, x2, y2 = point1
    lx1, hx1 = min(x1,x2), max(x1,x2)
    ly1, hy1 = min(y1,y2), max(y1,y2)


    if lx0 < lx1:
        xcheck = lx1 <= hx0
    else:
        xcheck = lx0 <= hx1

    if ly0 < ly1:
        ycheck = ly1 <= hy0
    else:
        ycheck = ly0 <= hy1
    
    return xcheck and ycheck 

def meet(point0, point1):
    
    a0, b0 = get_func(*point0)
    a1, b1 = get_func(*point1)
    
    if (a0 == "X" and a1 =="X") or (a0==a1):
        if b0 == b1:
            return check2(point0, point1)
        else:
            return False
    elif a0 == "X":
        cross_point = (b0, a1 * b0 + b1)
    elif a1 == "X":
        cross_point = (b1, a0 * b1 + b0)
    else:
        cross_point = ((b1 - b0) / (a0 - a1), (a0*b1 - b0*a1) / (a0 - a1))
    
    return check(cross_point, point0) and check(cross_point, point1)
    

result = [0 for _ in range(N)]

group_num = 0
def dfs(idx, group_num):
    now = points[idx]
    result[idx] = group_num

    for j in range(N):
        if result[j] == 0:
            if meet(now, points[j]):
                result[j] = group_num
                dfs(j, group_num)

for i in range(N):
    if result[i] == 0:
        group_num += 1
        dfs(i, group_num)

c = Counter(result)
print(len(c))
print(c.most_common(1)[0][1])

