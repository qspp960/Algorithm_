import sys
sys.setrecursionlimit(10**9)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m,k = map(int,sys.stdin.readline().split())
road = []
check = [[0 for _ in range(m)] for _ in range(n)]
answer = 0

for i in range(k):
    x,y = map(int,sys.stdin.readline().split())
    road.append((x-1,y-1))


def dfs(x,y,count):
    for i in range(len(road)):
        if check[road[i][0]][road[i][1]] == 0:
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if nx == road[i][0] and ny == road[i][1]:
                    check[road[i][0]][road[i][1]] = 1
                    count = dfs(road[i][0],road[i][1],count+1)

    global answer
    answer = max(answer,count)

    return count


for i in range(len(road)):
    if check[road[i][0]][road[i][1]] == 0:
        check[road[i][0]][road[i][1]] = 1
        dfs(road[i][0],road[i][1],1)
print(answer)