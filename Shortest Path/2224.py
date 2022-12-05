import sys
from collections import deque


n = int(sys.stdin.readline())
result = []
t = [[1e9] * 52 for _ in range(52)]

for i in range(n):
    r = list(map(str,sys.stdin.readline().split()))
    a = r[0]
    b = r[2]

    if ord(a) >= 97:
        a = ord(a) - 6
    else:
        a = ord(a)

    if ord(b) >= 97:
        b = ord(b) - 6
    else:
        b = ord(b)
    t[a-65][b-65] = 1

for x in range(52):
    for y in range(52):
        if x == y:
            t[x][y] = 0


for i in range(52):

    for x in range(52):
        for y in range(52):
            if t[x][y] > (t[x][i] + t[i][y]):
                t[x][y] = t[x][i] + t[i][y]

answer = 0
for x in range(52):
    for y in range(52):
        if t[x][y] < 1e9 and t[x][y] != 0:
            answer += 1
            a = x
            b = y
            if x > 25:
                a += 6
            if y > 25:
                b += 6
            result.append([chr(a+65),chr(b+65)])

print(answer)

for i in range(len(result)):
    if result[i][0] != result[i][1]:
        print(result[i][0] + " => " + result[i][1])
