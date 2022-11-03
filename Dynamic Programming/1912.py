n = int(input())

number = list(map(int,input().split()))

dp = [0] * n
dp[0] = number[0]

for i in range(1,n):
    if dp[i-1] < 0:
        if dp[i-1] < number[i]:
            dp[i] = number[i]
        else:
            dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + number[i]


print(max(dp))
