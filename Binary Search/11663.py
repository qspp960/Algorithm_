import sys

n, m = map(int,sys.stdin.readline().split())

dot = list(map(int,sys.stdin.readline().split()))
dot.sort()

line = []

for i in range(m):
    l = tuple(map(int,sys.stdin.readline().split()))
    line.append(l)

for i in range(n):

    line_first = line[i][0]
    line_last = line[i][1]

    start = 0
    end = len(line)-1

    while start <= end:
        middle = (start + end) // 2
        if line_first < dot[middle]:
            end = middle-1
        else:
            start = middle+1
    x = start

    start = 0
    end = len(line)-1
    while start <= end:
        middle = (start + end) // 2
        if line_last < dot[middle]:
            end = middle - 1
        else:
            start = middle + 1
    y = start
    result = y - x + 1
    print(y)
    print(x)
    #print(result)


