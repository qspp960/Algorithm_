import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    sticker = []
    s_1 = list(map(int,sys.stdin.readline().split()))
    sticker.append(s_1)
    s_2 = list(map(int,sys.stdin.readline().split()))
    sticker.append(s_2)

    dp = [[],[]]

    dp[0].append(sticker[0][0])
    dp[1].append(sticker[1][0])
    if n == 1:
        print(max(dp[0][n-1],dp[1][n-1]))
        continue
    dp[0].append(dp[1][0]+sticker[0][1])
    dp[1].append(dp[0][0]+sticker[1][1])

    for j in range(2,n):
        dp[0].append(max(dp[1][j-1],dp[1][j-2])+sticker[0][j])
        dp[1].append(max(dp[0][j-1],dp[0][j-2])+sticker[1][j])

    print(max(dp[0][n-1],dp[1][n-1]))
