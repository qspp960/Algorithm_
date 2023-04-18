import sys
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())

p = list(map(int,sys.stdin.readline().split()))
l = [[] for _ in range(n)]


for i in range(n-1):
    x,y = map(int,sys.stdin.readline().split())

    l[x-1].append(y-1)
    l[y-1].append(x-1)


dp = [[0,p[i]] for i in range(n)]
check = [0 for _ in range(n)]
answer = dp[0][1]


def dfs(current):
    check[current] = 1

    for i in range(len(l[current])):
        if check[l[current][i]] == 0:
            dfs(l[current][i])
            dp[current][0] += max(dp[l[current][i]][0],dp[l[current][i]][1])
            dp[current][1] += dp[l[current][i]][0]

    global answer
    answer = max(answer,dp[current][0],dp[current][1])


dfs(0)
print(answer)

