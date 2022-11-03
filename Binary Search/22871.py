n = int(input())

stone = list(map(int,input().split()))

dp = [0] * n

for i in range(1,n):
    min_k = 1e9
    max_k = []
    for j in range(0,i):
        max_k.append(max(dp[j],((i-j) * (1 + abs(stone[j]-stone[i])))))
    dp[i] = min(max_k)

print(dp[-1])

