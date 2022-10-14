import sys

n, m = map(int,sys.stdin.readline().split())

dx = {0,-1,-1}
dy = {-1,0,-1}

number = []

for i in range(n):
    num = list(map(int,sys.stdin.readline().split()))
    number.append(num)

prefix_sum = [[0] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        prefix_sum[i][j] = prefix_sum[i][j-1] + prefix_sum[i-1][j] + number[i-1][j-1] - prefix_sum[i-1][j-1]

for i in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())

    print(prefix_sum[x2][y2] - prefix_sum[x2][y1-1] - prefix_sum[x1-1][y2] + prefix_sum[x1-1][y1-1])
