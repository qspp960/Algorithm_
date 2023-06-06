import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())

y = [i for i in range(1,n+1)]

y = deque(y)
answer = []
k -= 1
while y:
    y.rotate(-k)
    answer.append(y.popleft())

result = "<"
for i in range(len(answer)):
    result += (str(answer[i]))
    if i != (len(answer)-1):
        result += ", "
result += ">"
print(result)