import sys

n, m = map(int,sys.stdin.readline().split())

path = []
path_cost = [[0] * n for _ in range(n)]
for i in range(n):
    p = list(map(int,sys.stdin.readline().split()))
    path.append(p)

for i in range(n):
    for j in range(n):
        if i != j and path[i][j] == 0:
            path_cost[i][j] = 1e9
        else:
            path_cost[i][j] = path[i][j]


for i in range(n):
    for x in range(n):
        for y in range(n):
            if path[x][y] > (path[x][i]+path[i][y]):
                path[x][y] = (path[x][i] + path[i][y])


for i in range(m):
    x,y,cost = map(int,sys.stdin.readline().split())

    if path[x-1][y-1] > cost:
        print("Stay here")

    else:
        print("Enjoy other party")