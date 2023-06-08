import sys

n = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

nge = [-1 for _ in range(n+1)]

stack = []
stack.append(0)

for i in range(1,n):
    while stack:
        if a[stack[-1]] < a[i]:
            nge[stack.pop()+1] = a[i]
            if len(stack) == 0:
                stack.append(i)
                break
        else:
            stack.append(i)
            break
nge = nge[1:]
print(' '.join(map(str,nge)))