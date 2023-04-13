import sys
sys.setrecursionlimit(100000)

n, m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
check = [0 for _ in range(n+1)]
answer = 0

for i in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(i):
    check[i] = 1
    for j in range(len(graph[i])):
        if check[graph[i][j]] == 0:
            dfs(graph[i][j])


for i in range(1,n+1):
    if check[i] == 0:
        dfs(i)
        answer += 1

print(answer)