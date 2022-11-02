import sys
from copy import deepcopy

direction = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

n,m,k = map(int,sys.stdin.readline().split())

fireball = [[[] for _ in range(n)] for _ in range(n)]
position = set()

for i in range(m):
    f = list(map(int,input().split()))

    position.add((f[0]-1,f[1]-1))
    fireball[f[0]-1][f[1]-1].append([f[2],f[3],f[4]])


for i in range(k):
    next_position = set()
    next_fireball = [[[] for _ in range(n)] for _ in range(n)]

    while position:
        r,c = position.pop()

        while fireball[r][c]:
            current_fb = fireball[r][c].pop()
            current_d = current_fb[2]
            current_s = current_fb[1]
            current_m = current_fb[0]

            c_r = r + (direction[current_d][0] * current_s)
            c_c = c + (direction[current_d][1] * current_s)

            c_r %= n
            c_c %= n

            next_position.add((c_r,c_c))
            next_fireball[c_r][c_c].append([current_m,current_s,current_d])

    for pos in next_position:
        current_r, current_c = pos

        if len(next_fireball[current_r][current_c]) > 1:
            sum_m = 0
            sum_s = 0
            sum_d = 0
            current_length = len(next_fireball[current_r][current_c])
            count_odd = 0
            count_even = 0

            while next_fireball[current_r][current_c]:
                current_fb = next_fireball[current_r][current_c].pop()
                sum_m += current_fb[0]
                sum_s += current_fb[1]
                sum_d += current_fb[2]

                if (current_fb[2] % 2) == 0:
                    count_even += 1
                elif (current_fb[2] % 2) != 0:
                    count_odd += 1
            if sum_m < 5:
                continue

            new_m = (sum_m // 5)
            new_s = (sum_s // current_length)
            new_d = []
            if (count_even == current_length) or (count_odd == current_length):
                new_d = [0,2,4,6]
            else:
                new_d = [1,3,5,7]

            for q in range(4):
                next_fireball[current_r][current_c].append([new_m,new_s,new_d[q]])

    position = deepcopy(next_position)
    fireball = deepcopy(next_fireball)

answer = 0

for pos in position:
    r,c = pos

    if len(fireball[r][c]) == 1:
        answer += fireball[r][c][0][0]

    elif len(fireball[r][c]) > 1:
        for v in range(len(fireball[r][c])):
            answer += fireball[r][c][v][0]

print(answer)


