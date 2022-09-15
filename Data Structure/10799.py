stick = list(input())
stack = []
ans = 0
for i in range(len(stick)):
    if stick[i] == '(':
        stack.append(stick[i])
    else:
        if stick[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            ans += 1
            stack.pop()

print(ans)