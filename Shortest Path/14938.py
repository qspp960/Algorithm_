import sys

n, m, l = map(int,sys.stdin.readline().split())

item = list(map(int,sys.stdin.readline().split()))

path = [[1e9] * n for _ in range(n)]

for i in range(l):
    a,b,c = map(int,sys.stdin.readline().split())
    a -= 1
    b -= 1
    path[a][b] = c
    path[b][a] = c


for i in range(n):
    for x in range(n):
        for y in range(n):
            current = path[x][y]
            if x != y and current > (path[x][i] + path[i][y]):
                path[x][y] = (path[x][i] + path[i][y])

result = 0
for x in range(n):
    answer = item[x]
    for y in range(n):
        if x != y and path[x][y] <= m:
            answer += item[y]

    if answer > result:
        result = answer

print(result)