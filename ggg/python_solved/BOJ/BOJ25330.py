N, K = map(int, input().split())

ans = 0
cost = list(map(int, input().split()))
reward = list(map(int, input().split()))
visited = [False] * N

village = list(zip(cost, reward))  # (체력, 보상)
village.sort()  # 첫 번째 요소 기준 자동 정렬


def dfs(health, saved, damage):
    global ans 
    ans = max(ans, saved)

    remain = sum(village[i][1] for i in range(N)
    if not visited[i] and damage + village[i][0] <= health)

    if saved + remain <= ans:
        return
    
    for i in range(N):
        if visited[i]: continue
        if health - village[i][0] - damage < 0: return

        visited[i] = True
        dfs(health - village[i][0] - damage, saved + village[i][1], damage + village[i][0])
        visited[i] = False

dfs(K,0,0)
print(ans)