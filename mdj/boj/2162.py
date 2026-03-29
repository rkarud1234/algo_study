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
import sys
sys.setrecursionlimit(100000)

N = int(input())

points = [list(map(int, input().split())) for _ in range(N)]

def get_func2(x1, y1, x2, y2):
    return y1 - y2, x1*y2 - x2*y1, x1 - x2

def check_intersection(point0, point1):
    # 두 점이 같은 직선 상인 경우 범위 체크
    x11, y11, x12, y12 = point0
    x21, y21, x22, y22 = point1

    # point0 기준
    lx1, hx1 = min(x11, x12), max(x11, x12)
    ly1, hy1 = min(y11, y12), max(y11, y12)

    lx2, hx2 = min(x21, x22), max(x21, x22)
    ly2, hy2 = min(y21, y22), max(y21, y22)

    # 축과 평행한 직선들 대비하여 x,y 모두 체크
    x1check = (lx1 <= x21 <= hx1) or (lx1 <= x22 <= hx1)
    y1check = (ly1 <= y21 <= hy1) or (ly1 <= y22 <= hy1)

    x2check = (lx2 <= x11 <= hx2) or (lx2 <= x12 <= hx2)
    y2check = (ly2 <= y11 <= hy2) or (ly2 <= y12 <= hy2)
    
    return (x1check and y1check) or (x2check and y2check)


def meet2(point0, point1):
    a0, b0, c0 = get_func2(*point0)
    a1, b1, c1 = get_func2(*point1)
    
    x1,y1,x2,y2 = point0
    is_point0_cross = (x1 * a1 + b1 - y1 * c1) * (x2 * a1 + b1 - y2 * c1) <= 0
    
    x1,y1,x2,y2 = point1
    is_point1_cross = (x1 * a0 + b0 - y1 * c0) * (x2 * a0 + b0 - y2 * c0) <= 0

    # 두번째 선분의 두점이 모두 첫번째 직선상에 있는 경우
    if (x1 * a0 + b0 - y1 * c0 == 0) and (x2 * a0 + b0 - y2 * c0 == 0):
        return check_intersection(point0, point1)
    
    return is_point0_cross and is_point1_cross



result = [0 for _ in range(N)]

group_num = 0
def dfs(idx, group_num):
    now = points[idx]
    result[idx] = group_num

    for j in range(N):
        if result[j] == 0:
            if meet2(now, points[j]):
                result[j] = group_num
                dfs(j, group_num)

for i in range(N):
    if result[i] == 0:
        group_num += 1
        dfs(i, group_num)


c = Counter(result)
print(len(c))
print(c.most_common(1)[0][1])

