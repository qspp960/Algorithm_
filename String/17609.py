import sys

n = int(sys.stdin.readline())


def check_palin(left,right):
    while left < right:
        if word[0][left] != word[0][right]:
            return False
        else:
            left += 1
            right -= 1
    return True


for i in range(n):
    word = sys.stdin.readline().split()
    length = len(word[0])

    left = 0
    right = length - 1
    check_zero = True
    check_one = False

    while left < right:
        if word[0][left] != word[0][right]:
            check_zero = False
            left_check = check_palin(left+1,right)
            right_check = check_palin(left,right-1)

            if left_check == True or right_check == True:
                check_one = True
                break
            else:
                break
        else:
            left += 1
            right -= 1

    if check_zero == True:
        print(0)
    elif check_one == True:
        print(1)
    else:
        print(2)

