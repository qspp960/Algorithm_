import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    p_graph = [[] for _ in range(n+1)]

    for j in range(n-1):
        a,b = map(int,sys.stdin.readline().split())
        p_graph[b].append(a)

    a,b = map(int,sys.stdin.readline().split())
    a_p = [a]
    b_p = [b]

    while True:
        if len(p_graph[a]) == 0:
            break
        a_p.append(p_graph[a][0])
        a = p_graph[a][0]

    while True:
        if len(p_graph[b]) == 0:
            break
        b_p.append(p_graph[b][0])
        b = p_graph[b][0]
    answer = 0

    for j in range(len(a_p)):
        if a_p[j] in b_p:
            answer = a_p[j]
            break
    print(answer)
