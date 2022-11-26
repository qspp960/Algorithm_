import sys
from itertools import combinations


n = int(sys.stdin.readline())
food = []
answer = 1e9

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    food.append((a,b))


for i in range(1,n+1):
    comb = list(combinations(food,i))

    for j in range(len(comb)):
        a = 1
        b = 0
        for k in range(len(comb[j])):
            a *= comb[j][k][0]
            b += comb[j][k][1]

        answer = min(answer,abs(a-b))

print(answer)


