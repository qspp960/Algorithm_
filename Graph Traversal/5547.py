import sys
from collections import deque

odd_dx = [-1,-1,0,0,1,1]
odd_dy = [0,1,-1,1,0,1]

even_dx = [-1,-1,0,0,1,1]
even_dy = [-1,0,-1,1,-1,0]
answer = 0
w, h = map(int,sys.stdin.readline().split())
house = [[0] * (w+2)]


for i in range(h):
    hs = deque(map(int,sys.stdin.readline().split()))
    hs.appendleft(0)
    hs.append(0)
    house.append(list(hs))

house.append([0] * (w+2))
visited = [[0] * (w+2) for _ in range(h+2)]


def dfs(x,y):
    global answer
    line = 0

    if (x % 2) == 0:
        for i in range(6):
            nx = x + even_dx[i]
            ny = y + even_dy[i]

            if 0 <= nx < (h+2) and 0 <= ny < (w+2):
                if house[nx][ny] == 0 and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        dfs(nx,ny)
                if house[nx][ny] == 1:
                    line += 1

    else:
        for i in range(6):
            nx = x + odd_dx[i]
            ny = y + odd_dy[i]

            if 0 <= nx < (h + 2) and 0 <= ny < (w + 2):
                if house[nx][ny] == 0 and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        dfs(nx, ny)
                if house[nx][ny] == 1:
                    line += 1

    if line != 6:
        answer += line


dfs(0,0)
visited[0][0] = 1


print(answer)
