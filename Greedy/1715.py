import sys
import heapq

n = int(sys.stdin.readline())

card = []
answer = 0

for i in range(n):
    g = int(sys.stdin.readline())
    heapq.heappush(card,g)

if len(card) == 1:
    print(0)
    exit(1)

while(True):
    if len(card) == 1:
        break
    first = heapq.heappop(card)
    second = heapq.heappop(card)
    answer += (first+second)
    heapq.heappush(card,first+second)

print(answer)
