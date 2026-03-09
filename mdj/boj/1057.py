N, a,b = map(int,input().split())

answer = 0

while a!=b:
    answer += 1
    a,b = (a-1)//2 + 1 , (b-1)//2 + 1
    
print(answer)