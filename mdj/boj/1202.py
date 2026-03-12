import bisect
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

switch = lambda x : [-1 * int(x[1]), int(x[0])]
jewelrys = [switch(input().split()) for _ in range(N)]
jewelrys.sort()

bags = [int(input()) for _ in range(K)]
bag_dict = {i:1 for i in range(K)}
bags.sort()

answer = 0
for jv, jm in jewelrys:
    if bags==[]:
        break

    idx = bisect.bisect_left(bags, jm)
    
    if idx == K:
        continue
    
    while bag_dict[idx]==0:
        idx += 1
        if idx >= K:
            idx -= 1
            break

    if bag_dict[idx]:
        bag_dict[idx] = 0
        answer += jv * -1

print(answer)


