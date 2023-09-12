import sys

n = int(sys.stdin.readline())

crane = list(map(int,sys.stdin.readline().split()))

b = int(sys.stdin.readline())

box = list(map(int,sys.stdin.readline().split()))

crane.sort()
box.sort()
check_box = [0] * len(box)
answer = 0

if max(crane) < max(box):
    print(-1)
    exit(0)

while True:
    for i in range(len(crane)):
        current = crane[i]
        for j in range(len(box)):
            if check_box[j] == 0:
                if current >= box[j]:
                    check_box[j] = 1
                break
            else:
                continue

    answer += 1

    if 0 not in check_box:
        break

print(answer)