import sys

n = int(sys.stdin.readline())
l = list(set(map(int,sys.stdin.readline().split())))

prime = [False,False] + [True] * 1000000

for i in range(2,len(prime)):
    if prime[i] == False:
        continue
        
    for j in range(2 * i, len(prime),i):
        if prime[j] == True:
            prime[j] = False

answer = 1

for i in range(len(l)):
    if prime[l[i]] == True:
        answer *= l[i]

if answer == 1:
    print(-1)
else:
    print(answer)


