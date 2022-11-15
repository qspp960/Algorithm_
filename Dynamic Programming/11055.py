import sys

n = int(sys.stdin.readline())

number = list(map(int,sys.stdin.readline().split()))

dp = [0] * n
dp[0] = number[0]

for i in range(1,n):
    for j in range(i):
        if number[i] > number[j]:
            dp[i] = max(dp[i],dp[j] + number[i])
        else:
            dp[i] = max(dp[i],number[i])
print(max(dp))



