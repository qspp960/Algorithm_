import sys
n = int(sys.stdin.readline())

dp = [0] * (n+1)

dp[1] = 0

for i in range(2,n+1):
    min_value = dp[i-1] + 1
    if i % 2 == 0:
        min_value = min(min_value,dp[i//2]+1)
    if i % 3 == 0:
        min_value = min(min_value,dp[i//3]+1)
    dp[i] = min_value
print(dp[n])