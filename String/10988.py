import sys

s = str(sys.stdin.readline().rstrip())

mid = int(len(s) // 2)

if s[:mid] == s[-1:-mid-1:-1]:
    print(1)
else:
    print(0)

