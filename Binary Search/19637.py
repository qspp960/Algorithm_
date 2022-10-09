import sys

n, m = map(int,sys.stdin.readline().split())

power = []

for i in range(n):
    a = tuple(map(str,sys.stdin.readline().split()))
    if power and power[-1][1] == a[1]:
        continue
    power.append((a[0],int(a[1])))

for i in range(m):
    ch = int(sys.stdin.readline())
    start = 0
    end = len(power)-1

    while start <= end:
        middle = (start+end) // 2

        if power[middle][1] < ch:
            start = middle + 1

        else:
            end = middle -1
    print(power[start][0])

