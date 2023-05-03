import sys
import copy
from collections import deque

n = int(sys.stdin.readline())
land = []
answer = 0
check = [[0 for _ in range(n)] for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

max_height = 1

for i in range(n):
    l = list(map(int,sys.stdin.readline().split()))
    max_height = max(max(l),max_height)
    land.append(l)


def bfs(c_land, c_check,height):
    result = 0
    for i in range(n):
        for j in range(n):
            q = deque()
            if c_land[i][j] > height and c_check[i][j] == 0:
                q.append((i,j))
                c_check[i][j] = 1
                result += 1
                while q:
                    current = q.pop()
                    for k in range(4):
                        nx = current[0] + dx[k]
                        ny = current[1] + dy[k]
                        if nx >= 0 and nx < n and ny >= 0 and ny < n:
                            if c_land[nx][ny] > height and c_check[nx][ny] == 0:
                                q.append((nx,ny))
                                c_check[nx][ny] = 1
    global answer
    answer = max(answer,result)


for i in range(1,max_height):
    bfs(copy.deepcopy(land),copy.deepcopy(check),i)

print(answer)