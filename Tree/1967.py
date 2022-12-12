import sys

sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
graph = [[] for _ in range(n)]

for i in range(n-1):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))

answer = 0
node_1 = 0
node_2 = 0


def dfs(start,count):
    visited[start] = 1
    for i in range(len(graph[start])):
        if visited[graph[start][i][0]] == 0:
            dfs(graph[start][i][0],count+graph[start][i][1])
    visited[start] = 0

    global answer, node_1, node_2
    if count > answer:
        answer = count
        node_1 = start
        node_2 = start


if n == 1:
    print(0)
    exit(0)
visited = [0] * n
dfs(0,0)
dfs(node_1,0)


print(answer)