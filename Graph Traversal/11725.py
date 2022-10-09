from collections import deque

n = int(input())

graph = [[] * (n+1) for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
parent_node = [0] * (n+1)
start = 1
dq = deque()
dq.append(start)
visited[start] = 1

while dq:
    st = dq.popleft()

    for q in graph[st]:
        if visited[q] == 0:
            dq.append(q)
            visited[q] = 1
            parent_node[q] = st

for i in range(2,len(parent_node)):
    print(parent_node[i])


