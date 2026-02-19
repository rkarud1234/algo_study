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
        # 지금 합이 S를 넘는다면
        # i와 j를 비교한다
        sum -= arr[l]
        l += 1
        cnt -= 1
    elif r < N: # 마지막 인덱스를 검사하기 위한 조건
        # 지금 합이 S를 안넘는다면
        sum += arr[r]
        r += 1
        cnt += 1
    else:
        l += 1

print(ans if ans != 1000000001 else 0)
