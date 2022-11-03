import sys

n = int(sys.stdin.readline())

x = list(map(int,sys.stdin.readline().split()))

dp = [0] * (n+1)
sum_number = x[0]

for i in range(1,n):

    dp[i] = sum_number * x[i] + dp[i-1]
    sum_number += x[i]
print(dp[n-1])