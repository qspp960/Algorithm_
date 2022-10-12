n = int(input())
dx = [0,0,1,1]
dy = [0,1,0,1]


pooling = []

for i in range(n):
    pool = list(map(int,input().split()))
    pooling.append(pool)

while True:
    next_polling = []
    for i in range(0,n,2):
        line_result = []
        for j in range(0,n,2):
            result = []
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                result.append(pooling[nx][ny])
            result.sort()
            line_result.append(result[-2])
        next_polling.append(line_result)
    pooling = next_polling
    n = n // 2
    if len(pooling) == 1:
        break
print(pooling[0][0])


