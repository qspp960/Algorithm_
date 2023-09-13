import sys

c,n = map(int,sys.stdin.readline().split())
city = []
for i in range(n):
    ct = tuple(map(int,sys.stdin.readline().split()))
    city.append(ct)

dp = [ 1e10 for _ in range(c+101)]
dp[0] = 0

for i in range(0,c+1):
    for j in range(len(city)):
        customer = city[j][1]
        money = city[j][0]
        dp[i+customer] = min(dp[i+customer],dp[i]+money)

print(min(dp[c:]))