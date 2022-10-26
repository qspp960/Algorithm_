n = int(input())

stair = []
dp = [0] * (n+1)

for i in range(n):
    s = int(input())
    stair.append(s)

dp[1] = stair[0]
if n >= 2:
    dp[2] = stair[0] + stair[1]

for i in range(3,n+1):
    dp[i] = max(dp[i-3]+stair[i-2]+stair[i-1],dp[i-2]+stair[i-1])

print(dp[n])
