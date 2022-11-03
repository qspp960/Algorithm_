n = int(input())

problem = input()
dp = [0] * n
dp[0] = 1

for i in range(1,len(problem)):
    if problem[i-1] == problem[i]:
        dp[i] = dp[i-1]
        continue
    else:
        if problem[0] == problem[i]:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + 1

print(dp[n-1])