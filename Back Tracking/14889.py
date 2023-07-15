import sys
import itertools

n = int(sys.stdin.readline())
people = []
answer = 1e10

for i in range(n):
    p = list(map(int,sys.stdin.readline().split()))
    people.append(p)

comb = [ i for i in range(n)]

nCr = list(itertools.combinations(comb,n//2))

for start in nCr:
    link = []
    link_score = 0
    start_score = 0
    for i in range(n):
        if i not in start:
            link.append(i)

    for i in range(len(link)):
        for j in range(i+1,len(link)):
            link_score += people[link[i]][link[j]]
            link_score += people[link[j]][link[i]]

    for i in range(len(start)):
        for j in range(i+1,len(start)):
            start_score += people[start[i]][start[j]]
            start_score += people[start[j]][start[i]]
    result = abs(start_score - link_score)

    if answer > result:
        answer = result

print(answer)