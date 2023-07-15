import sys

a,b,c = map(int,sys.stdin.readline().split())

dice = [ 0 for _ in range(7)]

dice[a] += 1
dice[b] += 1
dice[c] += 1

answer = 0
max_dice = 0
max_dot = 0
for i in range(1,len(dice)):
    if dice[i] != 0:
        if max_dice <= dice[i]:
            max_dice = dice[i]
            max_dot = i

if max_dice == 3:
    answer = 10000 + (max_dot * 1000)
elif max_dice == 2:
    answer = 1000 + (max_dot * 100)
else:
    answer = max_dot * 100

print(answer)