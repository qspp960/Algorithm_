r,c,t = map(int,input().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

room = []

machine = []
for i in range(r):
    a = list(map(int,input().split()))
    if a[0] == -1:
        machine.append(i)
    room.append(a)

while t > 0:
    after_room = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] >= 5 and room[i][j] != -1:
                count = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1:
                        count += 1
                        after_room[nx][ny] += (room[i][j] // 5)
                after_room[i][j] += room[i][j] - ((room[i][j] // 5) * count)
            elif room[i][j] < 5 and room[i][j] != -1:
                after_room[i][j] += room[i][j]
    up = machine[0]
    down = machine[1]

    for i in range(up-1,0,-1):
        after_room[i][0] = after_room[i-1][0]
    for i in range(c-1):
        if i == (c-1):
            after_room[0][i] = 0
        after_room[0][i] = after_room[0][i+1]
    for i in range(0,up):
        after_room[i][c-1] = after_room[i+1][c-1]

    for i in range(c-1,0,-1):
        after_room[up][i] = after_room[up][i-1]


    for i in range(down+1,r-1):
        after_room[i][0] = after_room[i+1][0]
    for i in range(c-1):
        after_room[r-1][i] = after_room[r-1][i+1]
    for i in range(r-1,down,-1):
        after_room[i][c-1] = after_room[i-1][c-1]
    for i in range(c-1,0,-1):
        after_room[down][i] = after_room[down][i-1]

    room = after_room
    room[machine[0]][0] = -1
    room[machine[1]][0] = -1
    t -= 1

result = 0
for rm in room:
    result += sum(rm)
print(result+2)





