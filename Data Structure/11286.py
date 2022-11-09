import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    m = int(sys.stdin.readline())

    if m != 0:
        heapq.heappush(heap,(abs(m),m))
    elif len(heap) == 0:
        print(0)
    else:
        print(heapq.heappop(heap)[1])
