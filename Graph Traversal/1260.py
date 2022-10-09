from collections import deque

n,m,v = map(int,input().split())

graph = [[] * (n+1) for _ in range(n+1)]
queue = deque()

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited = [0] * (n+1)
visited2 = [0] * (n+1)

bfs_result = []
dfs_result = []
queue.append(v)
visited2[v] = 1
bfs_result.append(v)
while queue:
    start = queue.popleft()
    for q in graph[start]:
        if visited2[q] == 0:
            queue.append(q)
            visited2[q] = 1
            bfs_result.append(q)


def dfs(start):
    visited[start] = 1
    dfs_result.append(start)

    for g in graph[start]:
        if visited[g] == 0:
            dfs(g)
dfs(v)
dfs_result = list(map(str,dfs_result))
bfs_result = list(map(str,bfs_result))
print(' '.join(dfs_result))
print(' '.join(bfs_result))