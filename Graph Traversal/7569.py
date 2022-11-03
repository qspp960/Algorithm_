import sys
from collections import deque

n,m,f = map(int,sys.stdin.readline().split())

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

tomato = []
dq = deque()

for i in range(f):
    f_tomato = []
    for j in range(m):
        t = list(map(int,sys.stdin.readline().split()))
        f_tomato.append(t)
        for k in range(n):
            if t[k] == 1:
                dq.append([i,j,k])
    tomato.append(f_tomato)

while dq:
    x,y,z = dq.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < f and 0 <= ny < m and 0 <= nz < n:
            if tomato[nx][ny][nz] == 0:
                tomato[nx][ny][nz] = (tomato[x][y][z] + 1)
                dq.append([nx,ny,nz])

answer = -1

for i in range(f):
    for j in range(m):
        for k in range(n):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)
            if tomato[i][j][k] > answer:
                answer = tomato[i][j][k]

print(answer-1)