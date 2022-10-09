n,m = map(int,input().split())

mx = [0,-1,-1,-1,0,1,1,1]
my = [-1,-1,0,1,1,1,0,-1]

dx = [-1,-1,1,1]
dy = [-1,1,-1,1]

basket = []
command = []

for i in range(n):
    b = list(map(int,input().split()))
    basket.append(b)

for i in range(m):
    a,b = map(int,input().split())
    command.append((a,b))

cloud = [[(n-1,0),(n-1,1),(n-2,0),(n-2,1)]]

for i in range(m):
    direction = command[i][0]-1
    move = command[i][1]
    visited = [[0] * n for _ in range(n)]
    for cld in cloud[i]:
        nx = (cld[0] + n + (mx[direction] * move)) % n
        ny = (cld[1] + n + (my[direction] * move)) % n
        visited[nx][ny] = 1
        basket[nx][ny] += 1

    next_cloud = []
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 1:
                for m in range(4):
                    nx = x + dx[m]
                    ny = y + dy[m]
                    if 0 <= nx < n and 0 <= ny < n and basket[nx][ny] >= 1:
                        basket[x][y] += 1

    for x in range(n):
        for y in range(n):
            if visited[x][y] == 0 and basket[x][y] >= 2:
                basket[x][y] -= 2
                next_cloud.append((x,y))
    cloud.append(next_cloud)


result = 0
for i in range(n):
    result += sum(basket[i])
print(result)

