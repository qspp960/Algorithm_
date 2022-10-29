import math

n = int(input())

dp = [0] * (n+1)

dp[0] = 0
dp[1] = 1


for i in range(2,n+1):
    sq = int(math.sqrt(i))
    value = 5
    for j in range(1,sq+1):
        value = min(value,dp[i-j**2])
    dp[i] = value + 1


print(dp[n])
