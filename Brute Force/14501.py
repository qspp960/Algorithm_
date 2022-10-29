n = int(input())

work = []
dp = [0] * (n+1)

for i in range(n):
    pt = list(map(int,input().split()))

    work.append(pt)

answer = -1

for i in range(n-1,-1,-1):
    if work[i][0] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],(work[i][1]+dp[work[i][0] + i]))

print(dp[0])


print(answer)
