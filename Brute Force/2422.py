import sys

n,m = map(int,sys.stdin.readline().split())

check = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())

    check[a][b] = 1
    check[b][a] = 1
result = 0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        for k in range(j+1,n+1):
            if check[i][j] == 0 and check[j][k] == 0 and check[i][k] == 0:
                result += 1
print(result)
