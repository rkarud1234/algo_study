# 문제
# IQ Test의 문제 중에는 공통된 패턴을 찾는 문제가 있다. 수열이 주어졌을 때, 다음 수를 찾는 문제이다.

# 예를 들어, 1, 2, 3, 4, 5가 주어졌다. 다음 수는 무엇인가? 당연히 답은 6이다. 약간 더 어려운 문제를 보면, 3, 6, 12, 24, 48이 주어졌을 때, 다음 수는 무엇인가? 역시 답은 96이다.

# 이제 제일 어려운 문제를 보자.

# 1, 4, 13, 40이 주어졌을 때, 다음 수는 무엇일까? 답은 121이다. 그 이유는 항상 다음 수는 앞 수*3+1이기 때문이다.

# 은진이는 위의 3문제를 모두 풀지 못했으므로, 자동으로 풀어주는 프로그램을 작성하기로 했다. 항상 모든 답은 구하는 규칙은 앞 수*a + b이다. 그리고, a와 b는 정수이다.

# 수 N개가 주어졌을 때, 규칙에 맞는 다음 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 N개의 수가 주어진다. 이 수는 모두 절댓값이 100보다 작거나 같은 정수이다.

# 출력
# 다음 수를 출력한다. 만약 다음 수가 여러 개일 경우에는 A를 출력하고, 다음 수를 구할 수 없는 경우에는 B를 출력한다.


N = int(input())

num_list = list(map(int, input().split()))


def solve(N, num_list):
    # 부정
    if N <= 1:
        return "A"

    # solve 
    a0, a1 = num_list[:2]
    if a0 == a1:
        # y 축과 평행한 케이스
        x,y = 1, 0
        check = 1
    elif N==2:
        # 부정
        return "A"
    else:
        # 두 점으로 기울기 구하기
        a2 = num_list[2]
        x = (a2-a1) / (a1-a0)
        y = (a1*a1 - a2*a0) / (a1 - a0)
        if (int(x) != x) | (int(y) != y):
            return "B"
        check = 2

    before = num_list[check]
    for next in num_list[check+1:]:
        if before * x + y != next:
            break
        before = next
    else:
        return int(before * x + y)
    return "B"
    
print(solve(N, num_list))