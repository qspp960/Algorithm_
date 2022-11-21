import sys

n = int(sys.stdin.readline())

dot = int(sys.stdin.readline())
dot_answer = []
result = [[0] * n for _ in range(n)]

number = n ** 2


def rotate(x,y,count):
    global number

    for i in range(count):
        if number == dot:
            dot_answer.append(x+1)
            dot_answer.append(y+1)

        result[x][y] = number
        number -= 1
        x += 1
    x -= 1
    y += 1

    for i in range(count-1):
        if number == dot:
            dot_answer.append(x+1)
            dot_answer.append(y+1)
        result[x][y] = number
        number -= 1
        y += 1
    y -= 1
    x -= 1

    for i in range(count-1):
        if number == dot:
            dot_answer.append(x + 1)
            dot_answer.append(y + 1)

        result[x][y] = number
        number -= 1
        x -= 1
    x += 1
    y -= 1

    for i in range(count-2):
        if number == dot:
            dot_answer.append(x + 1)
            dot_answer.append(y + 1)

        result[x][y] = number
        number -= 1
        y -= 1



r = n - 2
count = n
start_x = 0
start_y = 0
if n == 3:
    result[1][1] = 1
    if dot == 1:
        dot_answer.append(2)
        dot_answer.append(2)

for i in range(r):
    rotate(start_x,start_y,count)
    count -= 2
    start_x += 1
    start_y += 1

for i in range(n):
    print(' '.join(map(str,result[i])))

print(' '.join(map(str,dot_answer)))
