N = int(input())
nums = list(map(int, input().split()))

if N == 1:
    print('A')
elif len(set(nums)) == 1: # 모든 배열의 구성요소가 동일한 경우
    print(nums[0])
elif N == 2:
    print('A')
else:
    # 수열의 변동폭을 구하면 a를 알 수 있다.
    if nums[1] == nums[0] or (nums[2] - nums[1]) % (nums[1] - nums[0]) != 0:
        a = b = "err"
    else:
        a = (nums[2] - nums[1]) // (nums[1] - nums[0])
        b = nums[1] - a * nums[0]

    # 검증
    for i in range(1, N):
        if nums[i] != a * nums[i-1] + b:
            a = "err"
            break
    print("B" if a == "err" else nums[N - 1] * a + b)
