N, L = map(int, input().split())

for l in range(L, 101):
    if ((a1:=N/l-(l-1)/2) >= 0) and int(a1)==a1:
        a1 = int(a1)
        print(*range(a1, a1 + l), sep=' ')
        break
else:
    print(-1)