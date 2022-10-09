r,c,n = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,1,-1]

graph = []
bomb = [[0] * c for _ in range(r)]

for i in range(r):
    gr = input()
    gr_list = []
    for g in gr:
        gr_list.append(g)
    graph.append(gr_list)

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'O':
            bomb[i][j] = 1


for i in range(2,n+1):
    if i % 2 == 0:
        for j in range(r):
            for k in range(c):
                if graph[j][k] == '.':
                    graph[j][k] = 'O'
                    bomb[j][k] = 2
                else:
                    bomb[j][k] = 1
    else:
        for j in range(r):
            for k in range(c):
                if bomb[j][k] == 1:
                    graph[j][k] = '.'
                    bomb[j][k] = 0
                    for m in range(4):
                        nx = j + dx[m]
                        ny = k + dy[m]
                        if 0 <= nx < r and 0 <= ny < c:
                            if bomb[nx][ny] != 1:
                                graph[nx][ny] = '.'
                                bomb[nx][ny] = 0
for g in graph:
    print(''.join(g))