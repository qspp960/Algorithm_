computer = int(input())

n = int(input())

network = [[]*computer for _ in range(computer+1)]

for i in range(n):
    a,b = map(int,input().split())
    network[a].append(b)
    network[b].append(a)

count = 0
visited = [0] * (computer+1)


def dfs(start):
    global count
    visited[start] = 1
    for i in network[start]:
        if visited[i] == 0:
            dfs(i)
            count += 1
dfs(1)
print(count)






