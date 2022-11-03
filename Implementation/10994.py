n = int(input())


star = [[' '] * ((4*n)-3) for _ in range((4*n)-3)]

x = 0


def draw(start,end,number):
    for i in range(start,end):
        for j in range(start,end):
            if i == start or i == (end-1) or j == start or j == (end-1):
                star[i][j] = '*'
    if number == 1:
        return
    draw(start+2,end-2,number-4)


if n == 1:
    print("*")
    exit(0)
else:
    x = (4*n) - 3
    draw(0,x,x)
    for i in range(x):
        print(''.join(star[i]))



