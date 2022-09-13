from collections import deque


n = int(input())
dq = deque()

for i in range(1,n+1):
    dq.append(i)

while True:
    if len(dq) == 1:
        break
    dq.popleft()
    dq.append(dq.popleft())

print(dq.pop())