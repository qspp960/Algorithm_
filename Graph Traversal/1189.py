import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]

r,c,k = map(int,sys.stdin.readline().split())

land = []
answer = 0

for i in range(r):
    l = str(sys.stdin.readline())
    land.append(l)


def dfs(x,y,count,check):
    if count == k and x == 0 and y == (c-1):
        global answer
        answer += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < r and ny >= 0 and ny < c:
            if check[nx][ny] == 0 and land[nx][ny] != "T":
                check[nx][ny] = 1
                dfs(nx,ny,count+1,check)
                check[nx][ny] = 0


check = [[0 for _ in range(c)] for _ in range(r)]
check[r-1][0] = 1
dfs(r-1,0,1,check)
print(answer)