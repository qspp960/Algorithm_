import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

ground = []

for i in range(m):
    g = str(sys.stdin.readline())
    ground.append(g[:-1])

check = [ [0 for _ in range(n)] for _ in range(m)]

dq = deque()
dq.append((0,0,0))
check[0][0] = 1

while dq:
    current = dq.popleft()
    x = current[0]
    y = current[1]
    result = current[2]

    if x == (m - 1) and y == (n - 1):
        print(result)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < m and ny >= 0 and ny < n:
            if check[nx][ny] == 0:
                if ground[nx][ny] == "1":
                    dq.append((nx,ny,result+1))
                else:
                    dq.appendleft((nx,ny,result))
                check[nx][ny] = 1




