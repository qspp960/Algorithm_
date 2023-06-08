import sys
from collections import deque

n = int(sys.stdin.readline())

q = deque()

for i in range(n):
    c = list(map(str,sys.stdin.readline().split()))

    if len(c) == 2:
        q.append(c[1])
    else:
        if c[0] == "pop":
           if len(q) == 0:
               print(-1)
           else:
               print(q.popleft())

        elif c[0] == "size":
            print(len(q))

        elif c[0] == "empty":
            if len(q) == 0:
                print(1)
            else:
                print(0)

        elif c[0] == "front":
            if len(q) == 0:
                print(-1)
            else:
                print(q[0])

        elif c[0] == "back":
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])
