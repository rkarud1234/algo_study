pills = [[0] * 31 for _ in range(31)]

def go(W, H):
    if H < 0 or W < 0:
        return 0
    if W == 0:
        return 1
    
    if pills[W][H] == 0:
        pills[W][H] = go(W, H-1) + go(W-1, H+1)
    
    return pills[W][H]

go(30, 0)

while True:
    N = int(input())
    if N == 0:
        break
    print(pills[N][0])
