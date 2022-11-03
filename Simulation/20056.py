import sys
from copy import deepcopy

n,m,k = map(int,sys.stdin.readline().split())

direction = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

fireball = [[[] for _ in range(n)] for _ in range(n)]

fireball_position = set()

for i in range(m):
    f = list(map(int,sys.stdin.readline().split()))
    f[0] -= 1
    f[1] -= 1

    fireball[f[0]][f[1]].append([f[2],f[3],f[4]])
    fireball_position.add((f[0],f[1]))

for i in range(k):
    next_fireball_position = set()
    next_fireball = [[[] for _ in range(n)] for _ in range(n)]

    while fireball_position:
        current_r,current_c = fireball_position.pop()

        while fireball[current_r][current_c]:
            current_m, current_s, current_d = fireball[current_r][current_c].pop()

            current_r += (current_s * direction[current_d][0])
            current_c += (current_s * direction[current_d][1])

            current_r %= n
            current_c %= n

            next_fireball_position.add((current_r,current_c))
            next_fireball[current_r][current_c].append([current_m,current_s,current_d])
    print(next_fireball)
    for x in range(n):
        for y in range(n):
            if len(next_fireball[x][y]) >= 2:
                sum_m = 0
                sum_s = 0
                sum_d = 0
                count = 0
                while next_fireball[x][y]:
                    m,s,d = next_fireball[x][y].pop()
                    sum_m += m
                    sum_s += s
                    sum_d += d
                    count += 1
                sum_m //= 5
                sum_s //= count
                if sum_m == 0:
                    continue

                if (sum_d % 2) == 0:
                    for q in range(4):
                        next_fireball[x][y].append([sum_m,sum_s,q*2])
                else:
                    for q in range(4):
                        next_fireball[x][y].append([sum_m, sum_s, (q*2)+1])
    print(next_fireball)
    fireball = deepcopy(next_fireball)
    fireball_position = deepcopy(next_fireball_position)

answer = 0

for i in range(n):
    for j in range(n):
        if len(fireball[i][j]) == 1:
            answer += fireball[i][j][0][0]
        else:
            for k in range(len(fireball[i][j])):
                answer += fireball[i][j][k][0]
print(answer)







