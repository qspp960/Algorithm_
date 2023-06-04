import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n = int(sys.stdin.readline())
sea = []
shark = []
eat_cnt = 0
answer = 0
for i in range(n):
    s = list(map(int,sys.stdin.readline().split()))
    for j in range(len(s)):
        if s[j] == 9:
            shark.append(i)
            shark.append(j)
            shark.append(2)
    sea.append(s)

while True:
    dq = deque()
    dq.append((shark[0], shark[1], 0))
    visited = [[0 for _ in range(n)] for _ in range(n)]
    min_length = 1e9
    fish = []

    while dq:
        current = dq.popleft()
        visited[current[0]][current[1]] = 1

        for i in range(4):
            nx = current[0] + dx[i]
            ny = current[1] + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if visited[nx][ny] == 0 and sea[nx][ny] <= shark[2]:
                    dq.append((nx,ny,current[2]+1))
                    visited[nx][ny] = 1


                    if (current[2]+1) <= min_length and sea[nx][ny] < shark[2] and sea[nx][ny] > 0:
                        min_length = current[2] + 1
                        fish.append([nx,ny,current[2]+1])


    if len(fish) == 0:
        break
    target = fish[0]
    for i in range(1,len(fish)):
        if fish[i][0] < target[0]:
            target = fish[i]
        elif fish[i][0] == target[0] and fish[i][1] < target[1]:
            target = fish[i]

    eat_cnt += 1
    if shark[2] == eat_cnt:
        shark[2] += 1
        eat_cnt = 0

    sea[shark[0]][shark[1]] = 0
    sea[target[0]][target[1]] = 0
    shark[0] = target[0]
    shark[1] = target[1]
    answer += target[2]

print(answer)


