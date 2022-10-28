import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,sys.stdin.readline().split())
tomato = []
dq = deque()
visited = [[0] * n for _ in range(m)]
zero_count = 0

for i in range(m):
    t = list(map(int,sys.stdin.readline().split()))
    if 0 not in t:
        zero_count += 1
    if 1 in t:
        for j in range(len(t)):
            if t[j] == 1:
                dq.append([i,j,0])
                visited[i][j] = 1
    tomato.append(t)

if zero_count == m:
    print(0)
    exit(0)

while dq:
    x,y,c = dq.popleft()

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < m and 0 <= ny < n:
            if visited[nx][ny] == 0 and tomato[nx][ny] == 0:
                tomato[nx][ny] = (c+1)
                dq.append([nx,ny,c+1])
                visited[nx][ny] = 1

answer = -1
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0 and tomato[i][j] == 0:
            print(-1)
            exit(0)
        if answer < tomato[i][j]:
            answer = tomato[i][j]

print(answer)





