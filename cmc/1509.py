s = input()
n = len(s)
dp = [float("inf")] * 2501
# is_pal[i][j] : s[i:j] (슬라이스 그대로, j는 미포함)
is_pal = [[False for _ in range(n + 1)] for _ in range(n)]


def is_palindrome(string):
    return True if string == string[::-1] else False


for i in range(n):
    for j in range(i+1, n+1):
        if is_palindrome(s[i:j]):
            is_pal[i][j] = True

# dp[i] : s[0]~s[i-1]까지 i글자를 팰린드롬 조각으로만 나눌때, 필요한 조각 개수 최솟값
dp[0] = 0
for i in range(1, n+1):
    for j in range(0, i):
        if is_pal[j][i]:
            dp[i] = min(dp[i], dp[j]+1)
print(dp[n])
