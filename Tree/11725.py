import sys
from collections import deque

n = int(sys.stdin.readline())

edge = [[] for _ in range(n+1)]
tree = [[] for _ in range(n+1)]

dq = deque()
dq.append(1)

visited = [0] * (n+1)
visited[1] = 1

for i in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    edge[a].append(b)
    edge[b].append(a)

while dq:
    parent_node = dq.popleft()
    for i in range(len(edge[parent_node])):
        if visited[edge[parent_node][i]] == 0:
            visited[edge[parent_node][i]] = 1
            dq.append(edge[parent_node][i])
            tree[edge[parent_node][i]].append(parent_node)


for i in range(2,n+1):
    print(tree[i][0])