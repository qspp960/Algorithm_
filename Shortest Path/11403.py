import sys

n = int(sys.stdin.readline())
path = []
result = [[0] * n for _ in range(n)]

for i in range(n):
    p = list(map(int,sys.stdin.readline().split()))
    path.append(p)

for x in range(n):
    for y in range(n):
        if path[x][y] == 0:
            path[x][y] = 1e9


for i in range(n):
    for x in range(n):
        for y in range(n):
            path[x][y] = min(path[x][y],path[x][i]+path[i][y])


for x in range(n):
    for y in range(n):
        if path[x][y] == 1e9:
            path[x][y] = 0
        else:
            path[x][y] = 1

for i in range(n):
    result = list(map(str,path[i]))
    print(' '.join(result))