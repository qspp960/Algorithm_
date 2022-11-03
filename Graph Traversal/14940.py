import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
n,m = map(int,sys.stdin.readline().split())
path = []
answer = [[0] * m for _ in range(n)]

dq = deque()
start_x = 0
start_y = 0
for i in range(n):
    p = list(map(int,sys.stdin.readline().split()))

    if 2 in p:
        for j in range(m):
            if p[j] == 2:
                start_x = i
                start_y = j
    path.append(p)

answer = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dq.append([start_x,start_y,0])
visited[start_x][start_y] = 1

while dq:
    x,y,c = dq.popleft()
    answer[x][y] = c

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and path[nx][ny] == 1:
                dq.append([nx,ny,c+1])
                visited[nx][ny] = 1

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and path[i][j] == 1:
            answer[i][j] = -1

for i in range(n):
    print(' '.join(map(str,answer[i])))


