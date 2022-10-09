import sys

n, m = map(int,sys.stdin.readline().split())

dot = list(map(int,sys.stdin.readline().split()))
dot.sort()

line = []

for i in range(m):
    l = tuple(map(int,sys.stdin.readline().split()))
    line.append(l)

    lower = l[0]
    upper = l[1]

    start = 0
    end = len(dot)-1
    lower_start = 0
    while start <= end:
        middle = (start+end) // 2

        if lower < dot[middle]:
            lower_start = middle
            end = middle - 1
        elif lower == dot[middle]:
            lower_start = middle
            break
        else:
            lower_start = middle+1
            start = middle + 1
    start = 0
    end = len(dot) - 1
    upper_end = 0
    while start <= end:
        middle = (start+end) // 2
        if upper < dot[middle]:
            end = middle - 1
            upper_end = end
        elif upper == dot[middle]:
            upper_end = middle
            break
        else:
            start = middle + 1
            upper_end = middle

    if lower_start > upper_end:
        print(0)
    else:
        print(upper_end - lower_start + 1)


