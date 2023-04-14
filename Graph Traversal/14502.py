import copy
import sys
from collections import deque
sys.setrecursionlimit(100000)

dx = [-1,1,0,0]
dy = [0,0,1,-1]

n,m = map(int,sys.stdin.readline().split())

answer = 1e9
graph = []
virus = deque()
wall = 3
for i in range(n):
    g = list(map(int,sys.stdin.readline().split()))
    for j in range(m):
        if g[j] == 2:
            virus.append((i,j))
        elif g[j] == 1:
            wall += 1
    graph.append(g)


def bfs():
    t_virus = copy.deepcopy(virus)
    t_graph = copy.deepcopy(graph)
    result = 0
    while t_virus:
        result += 1
        current = t_virus.popleft()
        for i in range(4):
            nx = current[0] + dx[i]
            ny = current[1] + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and t_graph[nx][ny] == 0:
                t_graph[nx][ny] = 2
                t_virus.append((nx,ny))

    global answer
    answer = min(answer,result)


def make_wall(count):
    if count == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(count+1)
                graph[i][j] = 0

make_wall(0)
answer = ((n * m) - answer - wall)
print(answer)