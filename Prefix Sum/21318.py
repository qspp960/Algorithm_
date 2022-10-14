import sys

n = int(sys.stdin.readline())

level = list(map(int,sys.stdin.readline().split()))

q = int(sys.stdin.readline())
excuse = [0] * (n+1)

for i in range(len(level)):
    if i == 0:
        excuse[i+1] = 0
    else:
        if level[i] < level[i-1]:
            excuse[i+1] = excuse[i] + 1
        else:
            excuse[i+1] = excuse[i]
print(excuse)
for i in range(q):
    x,y = map(int,sys.stdin.readline().split())
    print(excuse[y]-excuse[x])
