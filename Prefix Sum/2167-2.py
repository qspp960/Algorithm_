n,m = map(int,input().split())

number = []

for i in range(n):
    num = list(map(int,input().split()))
    number.append(num)

k = int(input())

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = number[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

for v in range(k):
    i,j,x,y = map(int,input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])

