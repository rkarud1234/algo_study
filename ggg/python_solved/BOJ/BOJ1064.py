xA, yA, xB, yB, xC, yC = map(int, input().split())

def get_slope(x1, y1, x2, y2):
    if x1 == x2:
        return 0
    return (y2 - y1) / (x2 - x1)

def get_distance(x1, y1, x2, y2):
    import math
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 1. 세 점이 삼각형이 될 수 있는지 확인하기
if get_slope(xA, yA, xB, yB) == get_slope(xB, yB, xC, yC):
    print("-1.0")
    exit()

# 2. 각 변의 길이 계산하기
AB = get_distance(xA, yA, xB, yB)
BC = get_distance(xB, yB, xC, yC)
CA = get_distance(xC, yC, xA, yA)
max = max(AB, BC, CA)
min = min(AB, BC, CA)

# 3. 만들 수 있는 평행사변형 둘레 -> 두 변의 길이의 합 * 2
ans = (AB + BC + CA - min) * 2 - (AB + BC + CA - max) * 2
print(ans)