N = int(input())
k = int(input())

 # NxN행렬에서 숫자 n보다 작거나 같은 수가 몇개인지 세는 함수
def count_smaller(n):
    return sum(min(N, n//i) for i in range(1, min(N, n)+1))
l, r = 1, N*N
ans = None
# print('l mid r cnt')
# 이분탐색
while l<=r:
    mid = (l+r)//2
    cnt = count_smaller(mid)
    # print(l, mid, r, cnt)
    if cnt<k:
        l = mid+1
    elif cnt>=k:
        r = mid-1
        ans = mid

print(ans)