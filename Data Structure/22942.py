import sys

n = int(sys.stdin.readline())
circle = []

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())

    circle.append((a-b,i))
    circle.append((a+b,i))

circle.sort()
stack = []

for i in range(n*2):
    if len(stack) == 0:
        stack.append(circle[i])

    else:
        if stack[-1][1] == circle[i][1]:
            stack.pop()
        else:
            stack.append(circle[i])

if len(stack) == 0:
    print("YES")
else:
    print("NO")