import sys

n = int(sys.stdin.readline())
people = []

for i in range(n):
    p = tuple(map(int,sys.stdin.readline().split()))

    people.append(p)

answer = []

for i in range(n):
    count = 1
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            count += 1

    answer.append(count)

print(' '.join(map(str,answer)))


