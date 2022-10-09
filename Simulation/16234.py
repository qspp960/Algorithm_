from collections import deque
import sys

dx = [1,-1,0,0]
dy = [0,0,-1,1]

n,r,l = map(int,sys.stdin.readline().split())

country = []
result = 0
for i in range(n):
    c = list(map(int,sys.stdin.readline().split()))
    country.append(c)

while True:
    dq = deque()
    is_check = False
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                temp = []
                sum_country = 0
                count_country = 0
                visited[i][j] = 1
                dq.append((i,j))
                temp.append((i,j))
                while dq:
                    s_i = dq[0][0]
                    s_j = dq[0][1]
                    sum_country += country[s_i][s_j]
                    count_country += 1
                    dq.popleft()
                    for k in range(4):
                        nx = s_i + dx[k]
                        ny = s_j + dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            if visited[nx][ny] == 0 and r <= abs(country[s_i][s_j] - country[nx][ny]) <= l:
                                dq.append((nx,ny))
                                visited[nx][ny] = 1
                                temp.append((nx,ny))
                if len(temp) > 1:
                    is_check = True
                    for x,y in temp:
                        country[x][y] = sum_country // count_country
    if is_check == False:
        break
    result += 1
print(result)