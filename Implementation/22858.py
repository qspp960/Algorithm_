import sys
import copy

n,k = map(int,sys.stdin.readline().split())

s = list(map(int,sys.stdin.readline().split()))
d = list(map(int,sys.stdin.readline().split()))

p = [0 for _ in range(n)]
for i in range(k):
    for j in range(n):
        p[d[j]-1] = s[j]

    s = copy.deepcopy(p)

print(' '.join(map(str, p)))
