import sys
import heapq

n = int(sys.stdin.readline())
cs = []

for i in range(n):
    s,e = map(int,sys.stdin.readline().split())
    cs.append((s,e))

cs.sort()
queue = []
heapq.heappush(queue,cs[0][1])

for i in range(1,n):
    if queue[0] <= cs[i][0]:
        heapq.heappop(queue)
        heapq.heappush(queue,cs[i][1])
    else:
        heapq.heappush(queue,cs[i][1])


print(len(queue))