A, B = map(int, input().split())

dp = [0] * 60
sum = [0] * 60

dp[1] = 1
sum[1] = 1

for i in range(2, 60):
    dp[i] = sum[i-1] + pow(2, i-1)
    sum[i] = sum[i-1] + dp[i]

def recur(num, exp):
    if num == 0: return 0
    if num == 1: return 1

    next = num - (1 << (exp-1))
    if next == 0:
        return sum[exp-1] + 1
    else:
        return sum[exp-1] + recur(next, next.bit_length()) + next + 1

print(recur(B, B.bit_length()) - recur(A-1, (A-1).bit_length()))

