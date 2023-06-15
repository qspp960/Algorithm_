import sys

t = int(sys.stdin.readline())

for i in range(t):
    p = int(sys.stdin.readline())
    people = []

    for j in range(p):
        score = tuple(map(int,sys.stdin.readline().split()))
        people.append(score)

    people.sort(key=lambda x: x[0])
    answer = 1
    min_score = people[0][1]
    for k in range(1,len(people)):
        if min_score > people[k][1]:
            answer += 1
            min_score = people[k][1]

    print(answer)

