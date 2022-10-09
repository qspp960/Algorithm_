import math
import sys

n = int(sys.stdin.readline())

dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1

for i in range(2,n+1):
    min_num = 1e9
    for j in range(1,int(math.sqrt(i))+1):
        min_num = min(min_num,dp[i-j**2])
    dp[i] = min_num + 1
print(dp[n])

