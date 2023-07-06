import sys

n, m = map(int,sys.stdin.readline().split())
state = True
r,c,d = map(int,sys.stdin.readline().split())

ground = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

answer = 0

for i in range(n):
    g = list(map(int,sys.stdin.readline().split()))
    ground.append(g)


def clear(x,y):
    ground[x][y] = 2


def no_block(x,y,d):
    current_x = x
    current_y = y
    if d == 0:
        current_x += 1
    elif d == 1:
        current_y -= 1
    elif d == 2:
        current_x -= 1
    else:
        current_y += 1

    if current_x < 0 or current_x >= n or current_y < 0 or current_y >= m or ground[current_x][current_y] == 1:
        global state
        state = False
        return


while True:
    if ground[r][c] == 0:
        answer += 1
        clear(r,c)
        continue

    check = False

    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if ground[nx][ny] == 0:
                check = True
                break

    if check == False:
        no_block(r,c,d)

        if state == False:
            break
        else:
            if d == 0:
                r += 1
            elif d == 1:
                c -= 1
            elif d == 2:
                r -= 1
            else:
                c += 1
    else:
        for i in range(4):
            nx = r
            ny = c

            if d == 0:
                d = 3
            else:
                d -= 1

            if d == 0:
                nx = r - 1
            elif d == 1:
                ny = c + 1
            elif d == 2:
                nx = r + 1
            else:
                ny = c - 1

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if ground[nx][ny] == 0:
                    answer += 1
                    ground[nx][ny] = 2
                    r = nx
                    c = ny
                    break

print(answer)