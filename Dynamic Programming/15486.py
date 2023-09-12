import sys

n = int(sys.stdin.readline())

tp = []
dp = [0 for _ in range(n+2)]
for i in range(n):
    tp.append(tuple(map(int,sys.stdin.readline().split())))


for i in range(len(tp)):
    today = i + 1
    day = tp[i][0]
    score = tp[i][1]
    if today+day <= (n+1):
        dp[today+day] = max(dp[today+day], dp[today]+score)
    dp[today+1] = max(dp[today],dp[today+1])



print(dp[n+1])