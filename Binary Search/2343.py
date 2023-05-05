import sys

n, m = map(int,sys.stdin.readline().split())

b = list(map(int,sys.stdin.readline().split()))

start = 0
end = 1000000000

while start <= end:
    mid = (start + end) // 2

    if mid < max(b):
        start = mid + 1
        continue

    s_result = 0
    c_result = 1
    for i in range(len(b)):
        if (s_result + b[i]) <= mid:
            s_result += b[i]
        else:
            s_result = b[i]
            c_result += 1

    if c_result <= m:
        end = mid - 1
    else:
        start = mid + 1

print(start)

