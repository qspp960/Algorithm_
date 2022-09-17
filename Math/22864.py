import sys

a,b,c,m = map(int,sys.stdin.readline().split())

constraint = 0
work_hour = 0

for i in range(1,25):
    if constraint + a <= m:
        constraint += a
        work_hour += 1
    else:
        constraint -= c
        if constraint < 0:
            constraint = 0

print(work_hour*b)
