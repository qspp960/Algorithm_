n = int(input())

muscle = list(map(int,input().split()))

muscle.sort()
max_m = muscle[-1]

if (n%2) == 0:
    for i in range(0,n//2):
        if max_m < (muscle[i] + muscle[n-1-i]):
            max_m = (muscle[i] + muscle[n-1-i])
else:
    for i in range(0,(n-1)//2):
        if max_m < (muscle[i] + muscle[n-2-i]):
            max_m = (muscle[i] + muscle[n-2-i])

print(max_m)



