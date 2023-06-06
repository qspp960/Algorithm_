import sys

n = int(sys.stdin.readline())

dp = [ [ 0 for _ in range(10)] for _ in range(n+1)]

for i in range(len(dp[1])):
    dp[1][i] = 1

dp[1][0] = 0


for i in range(2,n+1):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

answer = 0
for i in range(len(dp[n])):
    answer += dp[n][i]

print(answer % 1000000000)