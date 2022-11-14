import sys

n, k = map(int,sys.stdin.readline().split())

child = list(map(int,sys.stdin.readline().split()))
tall = []

for i in range(len(child)-1):
    tall.append(child[i+1]-child[i])

tall.sort()

print(sum(tall[:n-k]))
