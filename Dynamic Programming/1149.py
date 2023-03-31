import sys

n = int(sys.stdin.readline())

h_cost = []

for i in range(n):
    cost = list(map(int,sys.stdin.readline().split()))
    h_cost.append(cost)

dp = [[1e9] * 3 for _ in range(n)]

dp[0][0] = h_cost[0][0]
dp[0][1] = h_cost[0][1]
dp[0][2] = h_cost[0][2]

for i in range(1,n):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + h_cost[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + h_cost[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + h_cost[i][2]


print(min(dp[n-1]))


