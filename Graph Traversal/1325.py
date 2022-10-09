from collections import deque

n, m = map(int,input().split())

graph = [[] * (n+1) for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)
dq = deque()
result = []
for i in range(1,n+1):
    count = 1
    visited = [0] * (n+1)
    visited[i] = 1
    dq.append(i)
    while dq:
        start = dq.popleft()
        for g in graph[start]:
            if visited[g] == 0:
                dq.append(g)
                visited[g] = 1
                count += 1
    result.append((i,count))

result.sort(key=lambda x: (-x[1],x[0]))
max_result = result[0][1]
real_result = []
for i in range(len(result)):
    if result[i][1] == max_result:
        real_result.append(str(result[i][0]))
    else:
        break
print(' '.join(real_result))


