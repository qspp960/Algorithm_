import sys
import heapq

n = int(sys.stdin.readline())
max_problem = []
min_problem = []

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    heapq.heappush(max_problem,(-b,-a))
    heapq.heappush(min_problem,(b,a))


o = int(sys.stdin.readline())
visited = [0] * 100001

for i in range(o):
    operation = list(map(str,sys.stdin.readline().split()))
    if operation[0] == "add":

        while max_problem:
            if visited[-max_problem[0][1]] == 1:
                heapq.heappop(max_problem)
            else:
                break

        while min_problem:
            if visited[min_problem[0][1]] == 1:
                heapq.heappop(min_problem)
            else:
                break

        heapq.heappush(max_problem,(-int(operation[2]),-int(operation[1])))
        heapq.heappush(min_problem,(int(operation[2]),int(operation[1])))
        visited[int(operation[1])] = 0

    elif operation[0] == "solved":
        visited[int(operation[1])] = 1
    else:
        if operation[1] == "1":
            while max_problem:
                if visited[-max_problem[0][1]] == 1:
                    heapq.heappop(max_problem)
                else:
                    break
            if max_problem and visited[-max_problem[0][1]] == 0:
                answer = max_problem[0][1]
                print(-answer)
        else:
            while min_problem:
                if visited[min_problem[0][1]] == 1:
                    heapq.heappop(min_problem)
                else:
                    break
            if min_problem and visited[min_problem[0][1]] == 0:
                answer = min_problem[0][1]
                print(answer)

