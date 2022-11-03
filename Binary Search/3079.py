import sys

n,m = map(int,sys.stdin.readline().split())

tk = []

for i in range(n):
    t = int(sys.stdin.readline())
    tk.append(t)

start = 0
end = (max(tk) * m)

while start <= end:

    count_m = 0
    middle = (start+end) // 2

    for i in range(n):
        count_m += (middle // tk[i])

    if count_m >= m:
        end = middle - 1

    elif count_m < m:
        start = middle + 1

print(start)