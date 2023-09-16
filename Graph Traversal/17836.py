import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m,t = map(int,sys.stdin.readline().split())

castle = []

for i in range(n):
    c = list(map(int,sys.stdin.readline().split()))
    castle.append(c)


check = [[0] * m for _ in range(n)]

q = deque()
q.append((0,0,0))
result = 100001
item = 100001
item_x = 0
item_y = 0
while q:
    current = q.popleft()
    check[current[0]][current[1]] = 1

    for i in range(4):
        nx = current[0] + dx[i]
        ny = current[1] + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if castle[nx][ny] == 2:
                if item > (current[2] + 1):
                    item = current[2] + 1
                    item_x = nx
                    item_y = ny
            if check[nx][ny] == 0 and castle[nx][ny] == 0:
                if nx == (n-1) and ny == (m-1):
                    if (current[2]+1) < result:
                        result = current[2]+1

                else:
                    q.append((nx,ny,current[2]+1))

answer = min(item + abs(n-1-item_x) + abs(m-1-item_y),result)
print(result)
if answer > t:
    print("Fail")
else:
    print(answer)