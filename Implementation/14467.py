n = int(input())

count = 0
cows = {}

for i in range(n):
    number, location = map(int,input().split())
    if number in cows:
        cows[number].append(location)
    else:
        cows[number] = [location]

for key,value in cows.items():
    for i in range(1,len(value)):
        if value[i] != value[i-1]:
            count += 1

print(count)
