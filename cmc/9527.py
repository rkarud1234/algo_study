# A, B = map(int, input().split())

def sum_of_ones(N):
    cnt=0
    n=1
    while n<=N:
        q=N//n
        r=N%n

        if q%2==1:
            cnt += n*(q//2) + r + 1
        else:
            cnt += n*(q//2)

        n*=2
    
    return cnt

print(sum_of_ones(4))
# print(sum_of_ones(B)-sum_of_ones(A-1))
