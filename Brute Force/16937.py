import sys

h,w = map(int,sys.stdin.readline().split())

n = int(sys.stdin.readline())
sticker = []
answer = 0

for i in range(n):
    rc = list(map(int,sys.stdin.readline().split()))
    sticker.append(rc)


for i in range(n-1):
    for j in range(i+1,n):
        first = sticker[i]
        second = sticker[j]

        if ((first[1] + second[1]) <= w and max(first[0],second[0]) <= h) or (max(first[0],second[0]) <= w and (first[1]+second[1]) <= h):
            result = (first[0]*first[1] + second[0] * second[1])
            answer = max(result,answer)

        elif ((first[1] + second[0]) <= w and max(first[0],second[1]) <= h) or (max(first[0],second[1]) <= w and (first[1]+second[0]) <= h):
            result = (first[0]*first[1] + second[0] * second[1])
            answer = max(result,answer)

        elif ((first[0] + second[1]) <= w and max(first[1],second[0]) <= h) or (max(first[1],second[0]) <= w and (first[0]+second[1]) <= h):
            result = (first[0]*first[1] + second[0] * second[1])
            answer = max(result,answer)

        elif ((first[0] + second[0]) <= w and max(first[1],second[1]) <= h) or (max(first[1],second[1]) <= w and (first[0]+second[0]) <= h):
            result = (first[0]*first[1] + second[0] * second[1])
            answer = max(result,answer)

print(answer)





