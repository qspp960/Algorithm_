import sys
from collections import deque

n = int(sys.stdin.readline())

l = list(map(int,sys.stdin.readline().split()))

if len(l) < 3:
    print(len(l))
    exit(1)

l.sort()

answer = 2

for k in range(2,len(l)):
   z = l[k]

   for i in range(k-1):
       x = l[i]
       y = l[i+1]

       if (x+y) > z:
           answer = max(answer,k-i+1)
           break
       else:
           continue


print(answer)


