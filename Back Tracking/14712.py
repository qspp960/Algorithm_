import sys
sys.setrecursionlimit(1000)

n,m = map(int,sys.stdin.readline().split())
nemo = [ [0] * (m+1) for _ in range(n+1)]

answer = 0


def dfs(x,y):
    count = 0

    if y >= (m+1):
        x += 1
        y = 1
    if x >= (n+1):
        return 0

    if nemo[x][y-1] == 0 or nemo[x-1][y-1] == 0 or nemo[x-1][y] == 0:
        nemo[x][y] = 1
        count += (dfs(x,y+1)+1)
        nemo[x][y] = 0
    count += dfs(x,y+1)

    return count


print(dfs(1,1)+1)








