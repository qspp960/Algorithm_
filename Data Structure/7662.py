import sys
import heapq

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    visited = [0] * n
    min_heap = []
    max_heap = []
    for j in range(n):
        op = list(map(str,sys.stdin.readline().split()))

        if op[0] == "I":
           heapq.heappush(min_heap,(int(op[1]),j))
           heapq.heappush(max_heap,(-int(op[1]),j))

        elif op[0] == "D":
            if op[1] == "1":
                while max_heap:
                    if visited[max_heap[0][1]] == 1:
                        heapq.heappop(max_heap)
                    else:
                        break

                if max_heap and visited[max_heap[0][1]] == 0:
                    visited[max_heap[0][1]] = 1
                    heapq.heappop(max_heap)

            elif op[1] == "-1":
                while min_heap:
                    if visited[min_heap[0][1]] == 1:
                        heapq.heappop(min_heap)
                    else:
                        break

                if min_heap and visited[min_heap[0][1]] == 0:
                    visited[min_heap[0][1]] = 1
                    heapq.heappop(min_heap)

    while max_heap:
        if visited[max_heap[0][1]] == 1:
            heapq.heappop(max_heap)
        else:
            break

    while min_heap:
        if visited[min_heap[0][1]] == 1:
            heapq.heappop(min_heap)
        else:
            break

    if len(max_heap) == 0:
        print("EMPTY")
    else:
        print(str(-max_heap[0][0]) + " " + str(min_heap[0][0]))







