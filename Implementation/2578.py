import sys

ground = []
number = []
result = 0
is_result = False
for i in range(5):
    gr = list(map(int,sys.stdin.readline().split()))
    ground.append(gr)
bingo = 0
count = 0

for i in range(5):
    num = list(map(int,sys.stdin.readline().split()))
    for j in range(5):
        count += 1
        chk = num[j]
        for k in range(5):
            for m in range(5):
                if ground[k][m] == chk:
                    ground[k][m] = 0
                    #check bingo
                    if sum(ground[k]) == 0:
                        bingo += 1

                    sum2 = 0
                    for n in range(5):
                        sum2 += ground[n][m]
                    if sum2 == 0:
                        bingo += 1
                    sum3 = 0
                    if k == m:
                        for n in range(5):
                            sum3 += ground[n][n]
                        if sum3 == 0:
                            bingo += 1
                    sum4 = 0
                    if k+m == 4:
                        for n in range(5):
                            sum4 += ground[4-n][n]
                        if sum4 == 0:
                            bingo += 1
        if is_result == False and bingo >= 3:
            result = count
            is_result = True
            break

print(result)






