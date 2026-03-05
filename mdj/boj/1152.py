# print(len(input().split()))
# 39824KB	48ms

# import sys
# print(len(sys.stdin.readline().split()))
# 39292KB	44ms

word = 0
answer = 0
for i in input():
    if i == " ":
        answer += word
        word = 0
    else:
        word = 1
answer += word
print(answer)

# 34368KB	144ms