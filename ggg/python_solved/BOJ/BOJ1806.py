N, S = map(int, input().split())
arr = list(map(int, input().split()))
l = 0
r = 1
sum = arr[0]
cnt = 1
ans = 1000000001

while l < N and r <= N:
    if sum >= S:
        ans = min(ans, cnt)
        sum -= arr[l]
        l += 1
        cnt -= 1
    elif r < N: # 마지막 인덱스를 검사하기 위한 조건
        sum += arr[r]
        r += 1
        cnt += 1
    else:
        l += 1

print(ans if ans != 1000000001 else 0)
