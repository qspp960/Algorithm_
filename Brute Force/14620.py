import sys
from itertools import combinations

n = int(sys.stdin.readline())
cost = []
ground = []
answer = 1e9
dx = [0,0,0,1,-1]
dy = [0,1,-1,0,0]


def flower_check(tp1,tp2):
    if tp1 == tp2:
        return False
    result = []
    for i in range(5):
        nx = tp1[0]+dx[i]
        ny = tp1[1]+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            result.append([nx,ny])
        else:
            return False

    for i in range(5):
        nx = tp2[0]+dx[i]
        ny = tp2[1]+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if [nx,ny] in result:
                return False
        else:
            return False
    return True


def check(tp):
    first = tp[0]
    second = tp[1]
    third = tp[2]
    if flower_check(first,second) and flower_check(first,third) and flower_check(second,third):
        money = 0
        for i in range(5):
            nx = first[0] + dx[i]
            ny = first[1] + dy[i]
            money += cost[nx][ny]

        for i in range(5):
            nx = second[0] + dx[i]
            ny = second[1] + dy[i]
            money += cost[nx][ny]

        for i in range(5):
            nx = third[0] + dx[i]
            ny = third[1] + dy[i]
            money += cost[nx][ny]

        global answer
        answer = min(answer,money)


for i in range(n):
    c = list(map(int,sys.stdin.readline().split()))
    cost.append(c)
    for j in range(n):
        ground.append((i,j))


gr = list(combinations(ground,3))


for i in range(len(gr)):
    check(gr[i])

print(answer)