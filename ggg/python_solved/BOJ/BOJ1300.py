N = int(input())
K = int(input())

def count(x):
    sum = 0
    for i in range(1, N+1):
        sum += min(x//i,N)
    return sum

l = 1
r = K
ans = 0
while l <= r:
    mid = (l+r)//2
    if count(mid) < K:
        l = mid + 1
    else:
        r = mid - 1
        ans = mid
        
print(ans)
        
