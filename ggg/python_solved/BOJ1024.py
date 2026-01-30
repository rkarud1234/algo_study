N, L = map(int, input().split())

def print_range(start, end):
    if start < 0 or end - start + 1 > 100:
        print('-1')
        return
    
    for i in range(start, end + 1):
        print(i, end= " ")

for i in range(L, 101):
    q = N // i
    r = N % i

    if i % 2 == 1 and r == 0:
        # 나머지가 0인 경우 -> 홀수만 가능
        print_range(q - (i // 2), q + (i // 2))
        exit()
    elif i % 2 == 0 and N % (2 * q + 1) == 0:
        # 나머지가 0이 아닌 경우 -> 몫 +1 했을 때의 값으로 나누어 떨어져야 함
        print_range(q - (i // 2) + 1, q + (i // 2))
        exit()
    
print("-1")
