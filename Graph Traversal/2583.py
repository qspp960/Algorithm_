import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

m,n,k = map(int,sys.stdin.readline().split())
dot = []
check = [[0 for _ in range(m)] for _ in range(n)]
answer = []

for i in range(k):
    d = list(map(int,sys.stdin.readline().split()))
    dot.append(d)


def check_dot(x,y):

    for i in range(len(dot)):
        x1 = dot[i][0]
        y1 = dot[i][1]
        x2 = dot[i][2]
        y2 = dot[i][3]

        if x >= x1 and x < x2 and y >= y1 and y < y2:
            return True
    return False


for i in range(n):
    for j in range(m):
        x = i
        y = j

        if check_dot(x,y) == False and check[x][y] == 0:
            dq = deque()
            dq.append((x,y))
            result = 0
            while dq:
                result += 1
                current = dq.popleft()
                cx = current[0]
                cy = current[1]
                check[cx][cy] = 1

                for w in range(4):
                    nx = cx + dx[w]
                    ny = cy + dy[w]

                    if nx >= 0 and nx < n and ny >= 0 and ny < m:
                        if check_dot(nx,ny) == False and check[nx][ny] == 0:
                            dq.append((nx,ny))
                            check[nx][ny] = 1
            answer.append(result)

answer.sort()
print(len(answer))
print(" ".join(map(str,answer)))






