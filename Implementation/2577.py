import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

result = str(a * b * c)
answer = [0 for _ in range(10)]

for i in range(len(result)):
    t = int(result[i])
    answer[t] += 1

for i in range(len(answer)):
    print(answer[i])

