import sys
from heapq import heappop,heappush

v, e = map(int,sys.stdin.readline().split())

start = int(sys.stdin.readline())
start -= 1
path = [[] for _ in range(v)]
path_cost = [1e9] * v


for i in range(e):
    x, y, c = map(int,sys.stdin.readline().split())
    path[x-1].append([c,y-1])


def djikstra():
    heap = []
    heappush(heap,[0,start])

    while heap:
        cost,current = heappop(heap)

        for i in range(len(path[current])):
            current_cost = cost + path[current][i][0]
            current_node = path[current][i][1]

            if path_cost[current_node] > current_cost:
                path_cost[current_node] = current_cost
                heappush(heap,[current_cost,current_node])


djikstra()
for i in range(v):
    if i == start:
        print(0)
    elif path_cost[i] == 1e9:
        print("INF")
    else:
        print(path_cost[i])



