import sys
import heapq

n = int(sys.stdin.readline())
heap = []


for i in range(n):
    c = int(sys.stdin.readline())

    if c == 0:
        if len(heap) == 0:
            print(0)

        else:
            print(heapq.heappop(heap))

    else:
        heapq.heappush(heap,c)


