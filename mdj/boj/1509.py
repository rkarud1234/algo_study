# 팰린드롬 분할
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	16316	8118	5870	48.605%
# 문제
# 세준이는 어떤 문자열을 팰린드롬으로 분할하려고 한다. 
# 예를 들어, ABACABA를 팰린드롬으로 분할하면, 
# {A, B, A, C, A, B, A}, {A, BACAB, A}, {ABA, C, ABA}, {ABACABA}등이 있다.

# 분할의 개수의 최솟값을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 문자열이 주어진다. 이 문자열은 알파벳 대문자로만 이루어져 있고, 최대 길이는 2,500이다.

# 출력
# 첫째 줄에 팰린드롬 분할의 개수의 최솟값을 출력한다.
import sys
sys.setrecursionlimit(10000)
from collections import defaultdict


s = input()
n = len(s)
pal_info = [[-1 if i!=j else 1 for i in range(n) ] for j in range(n)]


def check_pal(i,j):
    if i>=j:
        return 1
    
    if pal_info[i][j] != -1:
        return pal_info[i][j]
    elif s[i] == s[j]:
         ret = check_pal(i+1,j-1)
         pal_info[i][j] = ret
         return ret
    else:
        return 0

pal_dict = defaultdict(list)
for i in range(n):
    pal_dict[i].append(i)
    for j in range(i+1,n):
        if check_pal(i,j):
            pal_dict[i].append(j)


result = [i for i in range(n+1)]

for i in range(n):
    for j in pal_dict[i]:
        result[j+1] = min(result[i] + 1, result[j+1])

print(result[-1])

