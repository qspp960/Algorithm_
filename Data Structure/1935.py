import sys

n = int(sys.stdin.readline())

sentence = list(sys.stdin.readline())
ans = list()

for i in range(n):
    a = int(sys.stdin.readline())
    ans.append(a)

stack = []

for i in sentence:
    if 'A' <= i <= 'Z':
        stack.append(ans[ord(i)-ord('A')])

    elif i == '*':
        b = stack.pop()
        a = stack.pop()
        stack.append(a*b)
    elif i == '+':
        b = stack.pop()
        a = stack.pop()
        stack.append(a+b)
    elif i == '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a-b)
    elif i == '/':
        b = stack.pop()
        a = stack.pop()
        stack.append(a/b)
print('%.2f' %stack[0])




