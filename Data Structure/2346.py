import sys
from collections import deque

n = int(sys.stdin.readline())

balloon = deque(enumerate(map(int,sys.stdin.readline().split())))

result = []

while balloon:
    i,move = balloon.popleft()
    result.append(i+1)

    if move < 0:
        balloon.rotate(-move)

    elif move > 0:
        balloon.rotate(-(move-1))


print(' '.join(map(str,result)))






