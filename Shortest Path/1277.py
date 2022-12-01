import sys
import heapq
from collections import deque
from math import sqrt

n,w = map(int,sys.stdin.readline().split())
m = float(sys.stdin.readline())

e = []
line = [[] for _ in range(n)]

for i in range(n):
    x,y = map(int,sys.stdin.readline().split())

    e.append((x,y))

for i in range(w):
    a,b = map(int,sys.stdin.readline().split())
    line[a-1].append(b-1)
    line[b-1].append(a-1)

l_e = []

cost = [1e9] * n


def check():
    dq = deque()
    visited = [0] * n
    for i in range(n):
        l = []
        if len(line[i]) > 0:
            dq.append(i)
            l.append(i)
            visited[i] = 1
            while dq:
                c = dq.popleft()
                for j in range(len(line[c])):
                    if visited[line[c][j]] == 0:
                        dq.append(line[c][j])
                        l.append(line[c][j])
                        visited[line[c][j]] = 1
        if len(l) > 1:
            l_e.append(l)

cost[0] = 0
check()
q = []
q.append([0,0])
while q:
    current = heapq.heappop(q)
    start = current[1]
    for i in range(n):
        in_check = False
        if start != i:
            for j in range(len(l_e)):
                if start in l_e[j] and i in l_e[j]:
                    in_check = True
                    if cost[i] > cost[start]:
                        cost[i] = cost[start]
                        heapq.heappush(q,[-cost[i],i])
            if in_check == False:
                dx = e[start][0] - e[i][0]
                dy = e[start][1] - e[i][1]
                dx **= 2
                dy **= 2
                distance = sqrt(dx+dy)
                if distance > m:
                    continue
                distance += cost[start]
                if cost[i] > distance:
                    cost[i] = distance
                    heapq.heappush(q,[-distance,i])
print(int(cost[n-1]*1000))






