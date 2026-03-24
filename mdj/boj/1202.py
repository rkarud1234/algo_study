import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# switch = lambda x : [-1 * int(x[1]), int(x[0])]
jewelrys = [list(map(int, input().split())) for _ in range(N)]
jewelrys.sort()

bags = [int(input()) for _ in range(K)]
bag_dict = {i:[] for i in range(K)}
bags.sort()

jewelrys_candidate = []
jc_idx = 0

answer = 0
for bag in bags:
    while True:
        if jc_idx >= N:
            break
        mi, vi = jewelrys[jc_idx]
        if mi <= bag:
            heapq.heappush(jewelrys_candidate, -1 * vi)
            jc_idx += 1
        else:
            break
    
    if jewelrys_candidate:
        answer += heapq.heappop(jewelrys_candidate) * -1
    

print(answer)