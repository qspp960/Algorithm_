import sys
from collections import deque

n, m, k, x = map(int,sys.stdin.readline().split())

path = [[] for _ in range(n+1)]
cost = [int(1e9)] * (n+1)
visited = [0] * (n+1)
cost[x] = 0

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    path[a].append(b)

start = x
next_node = deque()
next_node.append(start)

while next_node:
    visited[start] = 1
    start = next_node.popleft()
    next = []
    for i in range(len(path[start])):
        current_cost = cost[start] + 1
        current_node = path[start][i]
        if current_cost < cost[current_node]:
            cost[current_node] = current_cost
            next.append(path[start][i])

    next.sort()
    for i in next:
        if visited[i] == 0:
            next_node.append(i)

result = 0
for i in range(1,len(cost)):
    if cost[i] == k:
        print(i)
        result += 1

if result == 0:
    print(-1)




