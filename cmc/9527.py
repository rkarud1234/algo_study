A, B = map(int, input().split())

def count_one(N):
    cnt=0
    n=1
    if N==0: return 0
    if N==1: return 1
    while n<=N:
        if n==1:
            cnt += (N+1)//2
        elif n==2:
            q = N//2
            if q%2==0:
                cnt += q
            else:
                cnt += N - q
        elif n>=4:
            q = N//n
            if q%2==0:
                cnt += (n//2)*q
            else:
                cnt += N - n*((q+1)//2) + 1
        n *= 2
    return cnt
print(count_one(B)-count_one(A-1))