import sys
import heapq

n = int(sys.stdin.readline())

heap = []
for i in range(n):
    number = list(map(int,sys.stdin.readline().split()))

    if len(heap) == 0:
        for j in range(n):
            heapq.heappush(heap,number[j])

    else:
        for j in range(n):
            if heap[0] < number[j]:
                heapq.heappop(heap)
                heapq.heappush(heap,number[j])

print(heap[0])







