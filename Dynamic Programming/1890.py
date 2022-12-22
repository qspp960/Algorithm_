import sys

n = int(sys.stdin.readline())

block = []
dp = [[0] * n for _ in range(n)]

for i in range(n):
    b = list(map(int,sys.stdin.readline().split()))
    block.append(b)

dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == (n-1) and j == (n-1):
            break
        if dp[i][j] != 0 and block[i][j] != 0:
            nx = j + block[i][j]
            ny = i + block[i][j]

            if 0 <= nx < n:
                dp[i][nx] += dp[i][j]
            if 0 <= ny < n:
                dp[ny][j] += dp[i][j]

print(dp[n-1][n-1])