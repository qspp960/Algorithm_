import sys

n = int(sys.stdin.readline())

s = list(map(int,sys.stdin.readline().split()))

l = []
l.append(s[0])
for i in range(1,len(s)):
    current = s[i]
    if current > l[-1]:
        l.append(current)

    else:
        start = 0
        end = len(l) - 1
        ret = 0
        while start <= end:
            mid = (start + end) // 2
            if l[mid] < current:
                start = mid + 1
            else:
                ret = mid
                end = mid - 1
        l[ret] = current

print(len(l))

