from heapq import heappop, heappush

n, k = map(int,input().split())

result = 0

path = [1e9] * 100001


def djikstra():
    heap = []
    heappush(heap,[0,n])
    path[n] = 0
    while heap:
        cost,start = heappop(heap)
        move_1 = start + 1
        move_2 = start - 1
        move_3 = start * 2


        if 0 <= move_1 <= 100000:
            if path[move_1] > (cost + 1):
                path[move_1] = (cost + 1)
                heappush(heap,[path[move_1],move_1])


        if 0 <= move_2 <= 100000:
            if path[move_2] > (cost + 1):
                path[move_2] = (cost + 1)
                heappush(heap,[path[move_2],move_2])


        if 0 <= move_3 <= 100000:
            if path[move_3] > (cost):
                path[move_3] = (cost)
                heappush(heap,[path[move_3],move_3])



if n >= k:
    result = n-k

else:
    djikstra()
    result = path[k]

print(result)
