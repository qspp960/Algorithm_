import sys

n = int(sys.stdin.readline())

tree = []

for i in range(n):
    t = list(map(int,sys.stdin.readline().split()))
    tree.append(t)

dp = [[0] * n for _ in range(n)]

dp[0][0] = tree[0][0]

if n == 1:
    print(dp[0][0])
    exit(0)

for i in range(1,n):
    for j in range(len(tree[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + tree[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + tree[i][j]

print(max(dp[n-1]))