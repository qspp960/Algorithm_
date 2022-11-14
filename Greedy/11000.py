import sys
import heapq

n = int(sys.stdin.readline())
cl = []

for i in range(n):
    s,e = map(int,sys.stdin.readline().split())
    cl.append([s,e])

#cl.sort(key=lambda x:(x[1],x[0]))
cl.sort()
room = []
heapq.heappush(room,cl[0][1])

for i in range(1,n):
    if cl[i][0] >= room[0]:
        heapq.heappop(room)
        heapq.heappush(room,cl[i][1])
    else:
        heapq.heappush(room,cl[i][1])


print(len(room))


