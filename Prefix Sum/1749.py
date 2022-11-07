import sys
from copy import copy

dx = [-1,0,-1]
dy = [0,-1,-1]

n, m = map(int,sys.stdin.readline().split())

board = [[0] * (m+1) for _ in range(n+1)]

for i in range(n):
    b = list(map(int,sys.stdin.readline().split()))

    for j in range(m):
        board[i+1][j+1] = b[j]

for i in range(1,n+1):
    for j in range(1,m+1):
        board[i][j] += (board[i-1][j] + board[i][j-1] - board[i-1][j-1])

print(board)
answer = -1e9

for i in range(1,n+1):
    for x in range(i,n+1):
        for y in range(1,m+1):
            for cy in range(1,y+1):
                check = board[x][y] - board[i][cy-1] - board[i-1][y] + board[x-1][cy-1]
                answer = max(answer,check)
print(answer)






