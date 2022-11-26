import sys

n = int(sys.stdin.readline())
dragon = []
ground = [[0] * 101 for _ in range(101)]


def check_dragon(x,y,d,g):
    dot = []
    if d == 0:
        dot.append((x,y))
        dot.append((x+1,y))
        ground[x][y] = 1
        ground[x+1][y] = 1
    elif d == 1:
        dot.append((x,y))
        dot.append((x,y-1))
        ground[x][y] = 1
        ground[x][y-1] = 1
    elif d == 2:
        dot.append((x,y))
        dot.append((x-1,y))
        ground[x][y] = 1
        ground[x-1][y] = 1
    elif d == 3:
        dot.append((x,y))
        dot.append((x,y+1))
        ground[x][y] = 1
        ground[x][y+1] = 1

    for i in range(g):
        last = dot[-1]
        for j in range(len(dot)-1,-1,-1):
            px = last[0] - dot[j][0]
            py = last[1] - dot[j][1]

            nx = last[0] + py
            ny = last[1] - px
            dot.append((nx,ny))
            ground[nx][ny] = 1


for i in range(n):
    x,y,d,g = map(int,sys.stdin.readline().split())
    check_dragon(x,y,d,g)


dx = [0,0,1,1]
dy = [0,1,0,1]
answer = 0
for i in range(100):
    for j in range(100):
        count = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if ground[nx][ny] == 1:
                count += 1
        if count == 4:
            answer += 1

print(answer)

