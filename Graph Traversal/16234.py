import sys
sys.setrecursionlimit(10**6)
dx = [0,0,-1,1]
dy = [1,-1,0,0]

n,l,r = map(int,sys.stdin.readline().split())

country = []


for i in range(n):
    c = list(map(int,sys.stdin.readline().split()))

    country.append(c)


def solution(x,y):
    global people
    people += country[x][y]
    result.append((x,y))
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0:
                check = abs(country[x][y] - country[nx][ny])
                if l <= check <= r:
                    global move_check
                    move_check = True
                    visited[nx][ny] = 1
                    solution(nx,ny)

answer = 0
while True:
    answer += 1
    visited = [[0] * n for _ in range(n)]
    move_check = False
    for i in range(n):
        for j in range(n):
            result = []
            if visited[i][j] == 0:
                people = 0
                visited[i][j] = 1
                solution(i,j)
                p = people // len(result)
                for k in range(len(result)):
                    country[result[k][0]][result[k][1]] = p

    if move_check == False:
        break
print(answer-1)