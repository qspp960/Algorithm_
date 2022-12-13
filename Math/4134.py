import sys

t = int(sys.stdin.readline())


def check(number):
    if number == 0 or number == 1:
        return False

    for i in range(2,(int(number**0.5) + 1)):
        if (number % i) == 0:
            return False
    return True


for i in range(t):
    n = int(sys.stdin.readline())
    number = n
    while True:
        if check(number) == True:
            print(number)
            break
        else:
            number += 1


