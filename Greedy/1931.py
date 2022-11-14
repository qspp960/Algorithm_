import sys


t = int(sys.stdin.readline())

cl = []

for i in range(t):
    s,e = map(int,sys.stdin.readline().split())
    cl.append([s,e])

cl.sort(key=lambda x:(x[1],x[0]))
end = cl[0][1]
answer = 1
for i in range(1,len(cl)):
    if cl[i][0] >= end:
        answer += 1
        end = cl[i][1]

print(answer)