import sys
from collections import deque

t = int(sys.stdin.readline())

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def solve(m, n, c_ground, c_check):
    answer = 0

    for i in range(n):
        for j in range(m):
            if c_check[i][j] == 0 and c_ground[i][j] == 1:
                answer += 1
                dq = deque()
                dq.append((i,j))
                c_check[i][j] = 1
                while dq:
                    current = dq.popleft()

                    for k in range(4):
                        nx = current[0] + dx[k]
                        ny = current[1] + dy[k]

                        if nx >= 0 and nx < n and ny >= 0 and ny < m and c_ground[nx][ny] == 1 and c_check[nx][ny] == 0:
                            dq.append((nx,ny))
                            c_check[nx][ny] = 1
    print(answer)


for i in range(t):
    m,n,k = map(int,sys.stdin.readline().split())
    ground = [[0 for _ in range(m)] for _ in range(n)]
    check = [[0 for _ in range(m)] for _ in range(n)]

    for j in range(k):
        y,x = map(int,sys.stdin.readline().split())
        ground[x][y] = 1

    solve(m,n,ground,check)
