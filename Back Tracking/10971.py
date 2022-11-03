n = int(input())

city = []

for i in range(n):
    c = list(map(int,input().split()))
    city.append(c)

travel = []
visited = [0] * n
sum_cost = []


def dfs(start,cost):
    if len(travel) == n:
        if city[travel[-1]][travel[0]] != 0:
            cost += city[travel[-1]][travel[0]]
            sum_cost.append(cost)
        return

    for i in range(n):
        if visited[i] == 0 and city[start][i] > 0 and i not in travel:
            travel.append(i)
            visited[i] = 1
            cost += city[start][i]
            dfs(i,cost)
            cost -= city[start][i]
            visited[i] = 0
            travel.pop()


for i in range(n):
    cost = 0
    travel.append(i)
    visited[i] = 1
    dfs(i,cost)
    travel.pop()
    visited[i] = 0

print(min(sum_cost))