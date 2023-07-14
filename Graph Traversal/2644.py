import sys

n = int(sys.stdin.readline())

s,t = map(int,sys.stdin.readline().split())
s -= 1
t -= 1

m = int(sys.stdin.readline())

parent = [[] for _ in range(n)]

answer = 0


def dfs(current,result):
    if current == t:
        global answer
        answer = result

    for i in range(len(parent[current])):
        if check[parent[current][i]] == 0:
            check[parent[current][i]] = 1
            dfs(parent[current][i],result+1)
            check[parent[current][i]] = 0


for i in range(m):
    p,c = map(int,sys.stdin.readline().split())
    p -= 1
    c -= 1

    parent[p].append(c)
    parent[c].append(p)


check = [0 for _ in range(n)]

check[s] = 1

for i in range(len(parent[s])):
    check[parent[s][i]] = 1
    dfs(parent[s][i],1)

if answer == 0:
    answer = -1

print(answer)

