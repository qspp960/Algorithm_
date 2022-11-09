import heapq
import sys

n = int(sys.stdin.readline())

max_heap = []

for i in range(n):
    s = int(sys.stdin.readline())

    if s > 0:
        heapq.heappush(max_heap,-s)

    else:
        if len(max_heap) == 0:
            print(0)
        else:
            answer = heapq.heappop(max_heap)
            print(-answer)

