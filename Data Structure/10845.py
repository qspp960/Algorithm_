import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

for i in range(n):
    cmd = list(map(str,sys.stdin.readline().split()))
    if cmd[0] == "push":
        q.append(cmd[1])

    else:
        if cmd[0] == "pop":
            if len(q) == 0:
                print("-1")
            else:
                print(q.popleft())

        elif cmd[0] == "size":
            print(len(q))

        elif cmd[0] == "empty":
            if len(q) == 0:
                print("1")
            else:
                print("0")

        elif cmd[0] == "front":
            if len(q) == 0:
                print("-1")

            else:
                print(q[0])

        else:
            if len(q) == 0:
                print("-1")
            else:
                print(q[-1])
