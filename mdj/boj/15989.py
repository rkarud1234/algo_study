N = int(input())

two = [-1 for _ in range(10000)]
three = [-1 for _ in range(10000)]

two[0], three[0] = 0, 0
two[1], three[1] = 1, 0
two[2], three[2] = 1, 1


for now in range(3, 10000):
    two[now] = two[now-2] + 1
    three[now] = three[now-3] + two[now-3] + 1

for _ in range(N):
    t = int(input())
    print(1 + two[t-1] + three[t-1])
