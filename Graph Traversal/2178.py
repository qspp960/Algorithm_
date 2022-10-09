from collections import deque

n, m = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,1,-1]
miro = []
path_count = [[0]*m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for i in range(n):
    road = input()
    miro.append(road)


def bfs():
    dq = deque()
    dq.append((0,0))
    path_count[0][0] = 1
    visited[0][0] = 1
    while dq:
        start = dq.popleft()
        a = start[0]
        b = start[1]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and miro[nx][ny] == '1':
                    dq.append((nx,ny))
                    visited[nx][ny] = 1
                    path_count[nx][ny] = path_count[a][b] + 1
bfs()
print(path_count[n-1][m-1])





