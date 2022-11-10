import sys
from collections import deque

n, w = map(int,sys.stdin.readline().split())

node = [[] for _ in range(n+1)]

for i in range(n-1):
    u,v = map(int,sys.stdin.readline().split())

    node[u].append(v)
    node[v].append(u)

dq = deque()
visited = [0] * (n+1)
dq.append(1)
visited[1] = 1
leaf_count = 0

while dq:
    current = dq.popleft()
    leaf_check = True

    for i in range(len(node[current])):
        if visited[node[current][i]] == 0:
            dq.append(node[current][i])
            visited[node[current][i]] = 1
            leaf_check = False

    if leaf_check == True:
        leaf_count += 1

print(w/leaf_count)
