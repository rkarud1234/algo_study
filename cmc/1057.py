N, A, B = map(int, input().split())
cnt=0

while True:
    if A==B:
        break
    
    if A==N:
        A = A//2 if A%2==0 else (A+1)//2
    else:
        A = (A+1)//2
    if B==N:
        B = B//2 if B%2==0 else (B+1)//2
    else:
        B = (B+1)//2
        
    N = N//2 if N%2==0 else (N+1)//2
    # print(N, A, B)
    cnt+=1
    
print(cnt)