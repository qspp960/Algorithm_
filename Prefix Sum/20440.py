import sys
from collections import defaultdict, OrderedDict

n = int(sys.stdin.readline())
mos = defaultdict(int)

for i in range(n):
    s,t = map(int,sys.stdin.readline().split())
    mos[s] += 1
    mos[t] -= 1

mos = OrderedDict(sorted(mos.items(), key=lambda x: x[0]))

max_count = -1
cur_count = 0
start = 0
end = 0
max_check = False

for k,v in mos.items():
    cur_count += v

    if max_count < cur_count:
        max_count = cur_count
        max_check = True
        start = k

    elif max_count > cur_count and max_check == True:
        max_check = False
        end = k


print(max_count)
print(str(start),str(end))
