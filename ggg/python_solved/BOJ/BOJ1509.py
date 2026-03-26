s = input()
LEN = len(s)
arr = [LEN] * (LEN+1)
arr[LEN] = 0

def palindrome(l, r):
    while l >= 0 and r < LEN:
        if s[l] != s[r]:
            break
        arr[r] = min(arr[l-1] + 1, arr[r])
        l = l-1
        r = r+1

for i in range(LEN):
    palindrome(i, i) # 홀수인 경우
    palindrome(i-1, i) # 짝수인 경우

    arr[i] = min(arr[i-1] + 1, arr[i])

print(arr[LEN-1])
