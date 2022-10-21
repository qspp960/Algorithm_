import sys

n = int(sys.stdin.readline())

tower = list(map(int,sys.stdin.readline().split()))

stack = []
answer = []

for i in range(len(tower)):
    if not stack:
        answer.append(0)
        stack.append((tower[i],i))

    else:
        while stack:
            if tower[i] < stack[-1][0]:
                answer.append(stack[-1][1]+1)
                stack.append((tower[i],i))
                break
            elif tower[i] >= stack[-1][0]:
                stack.pop()
        if not stack:
            answer.append(0)
            stack.append((tower[i],i))


print(' '.join(map(str,answer)))





