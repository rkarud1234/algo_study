# 책 페이지
 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	24780	8655	7075	44.059%
# 문제
# 지민이는 전체 페이지의 수가 N인 책이 하나 있다. 
# 첫 페이지는 1 페이지이고, 마지막 페이지는 N 페이지이다. 각 숫자가 전체 페이지 번호에서 모두 몇 번 나오는지 구해보자.

# 입력
# 첫째 줄에 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 0이 총 몇 번 나오는지, 1이 총 몇 번 나오는지, ..., 9가 총 몇 번 나오는지를 공백으로 구분해 출력한다.

n = int(input())

num_cnt = [0 for i in range(10)]

def kth_count(num, k):
    # 10**k번째 자리수둘의 등장 횟수 세는 함수

    # front : 현재 자리보다 앞 수, back : 현재자리 보다 뒷수
    front, left = divmod(num, 10**(k+1))
    now, back = divmod(left, 10**k)

    # 0은 맨 앞에 올 수 없어서 처음에만 1식 빼줌
    zero_flag = 1
    for i in range(10):
        if i < now:
            num_cnt[i] += (front + 1 - zero_flag) * 10**k
        elif i > now:
            num_cnt[i] += (front) * 10**k
        else:
            num_cnt[i] += (front - zero_flag) * 10**k + back+1
        zero_flag = 0

for i in range(len(str(n))):
    kth_count(n, i)

print(" ".join(map(str,num_cnt)))
