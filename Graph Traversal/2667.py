n = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

village = []

for i in range(n):
    home = input()
    village.append(home)

visited = [[0] * n for _ in range(n)]

count = [0] * (25*25)
cnt = 0


def dfs(i,j):
    visited[i][j] = 1
    count[cnt] += 1
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and village[nx][ny] == '1':
                dfs(nx,ny)


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and village[i][j] == '1':
            dfs(i,j)
            cnt += 1

count = count[:cnt]
print(len(count))
count.sort()
for r in count:
    print(r)



