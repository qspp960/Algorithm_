import sys

n = int(sys.stdin.readline())


bj = []
sj = []

for i in range(n-1):
    s,b = map(int,sys.stdin.readline().split())

    bj.append(b)
    sj.append(s)

k = int(sys.stdin.readline())

if n == 1:
    print(0)
    exit(0)

if n == 2:
    print(sj[0])
    exit(0)
dp = [1e9] * (n+1)
dp[0] = 0
dp[1] = 0
dp[2] = sj[0]
dp[3] = min(dp[2]+sj[1],dp[1]+bj[0])

for i in range(4,n+1):
    dp[i] = min(dp[i-1]+sj[i-2],dp[i-2]+bj[i-3])

min_answer = dp[n]
for i in range(4,n+1):
    dp_copy = dp[:]
    dp_copy[i] = min(dp[i],dp[i-3]+k)
    for j in range(i, n + 1):
        dp_copy[j] = min(dp_copy[j],dp_copy[j - 1] + sj[j - 2], dp_copy[j - 2] + bj[j - 3])

    if dp_copy[n] < min_answer:
        min_answer = dp_copy[n]

print(min_answer)
