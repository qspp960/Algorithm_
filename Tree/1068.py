import sys
from collections import deque

n = int(sys.stdin.readline())

parent = list(map(int,sys.stdin.readline().split()))
node = [[] for _ in range(n)]
root = 0
rm_node = int(sys.stdin.readline())

for i in range(len(parent)):
    if parent[i] == -1:
        root = i
    else:
        node[parent[i]].append(i)


dq = deque()
dq.append(root)
visited = [0] * n
visited[root] = 1
answer = 0

while dq:
    current = dq.popleft()
    count = 0

    for i in range(len(node[current])):
        if node[current][i] != rm_node:
            count += 1

    if current != rm_node and count == 0:
        answer += 1
        continue

    for i in range(len(node[current])):
        if current != rm_node and visited[node[current][i]] == 0 and node[current][i] != rm_node:
            dq.append(node[current][i])
            visited[node[current][i]] = 1

print(answer)
