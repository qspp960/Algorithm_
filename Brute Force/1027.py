import sys

n = int(sys.stdin.readline())

b = list(map(int,sys.stdin.readline().split()))

answer = 0

for i in range(n):
    left = i - 1
    right = i + 1
    count = 0
    current = b[i]
    shy = 0
    ex_shy = None
    for x in range(left,-1,-1):
        shy = (b[x]-b[i]) / (x - i)
        if ex_shy is None or shy < ex_shy:
            count += 1
            ex_shy = shy

    ex_shy = None
    for y in range(right,n):
        shy = (b[y] - b[i]) / (y - i)
        if ex_shy is None or shy > ex_shy:
            count += 1
            ex_shy = shy

    answer = max(answer,count)

print(answer)