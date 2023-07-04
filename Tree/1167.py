import sys

n = int(sys.stdin.readline())
tree = [[] for _ in range(n)]
answer = 0
node = 0

for i in range(n):
    t = list(map(int,sys.stdin.readline().split()))
    for j in range(1,len(t)-1):
        if (j % 2) == 0:
            tree[t[0]-1].append((t[j-1]-1,t[j]))
check = [ 0 for _ in range(n)]


def dfs(current,result):
    global answer
    global node
    if result > answer:
        answer = result
        node = current

    for i in range(len(tree[current])):
        if check[tree[current][i][0]] == 0:
            check[tree[current][i][0]] = 1
            dfs(tree[current][i][0],result+tree[current][i][1])
            check[tree[current][i][0]] = 0


check[0] = 1
dfs(0,0)
check[0] = 0
check[node] = 1
dfs(node,0)


print(answer)
