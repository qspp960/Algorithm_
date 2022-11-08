import sys

n,m = map(int,sys.stdin.readline().split())

words = {}

for i in range(n):
    w = sys.stdin.readline()
    words[w] = 1

answer = 0

for i in range(m):
    w = sys.stdin.readline()

    if w in words:
        answer += 1

print(answer)

