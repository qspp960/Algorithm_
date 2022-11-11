a, b = map(int,input().split())

answer = 0


def solution(number,count):
    if number == a:
        global answer
        answer = count + 1
        return
    elif number < a:
        return

    str_number = str(number)

    if str_number[-1] == '1':
        solution(int(str_number[:-1]),count+1)
    elif (number % 2) == 0:
        solution(number//2,count+1)
    else:
        return


solution(b,0)
if answer == 0:
    print(-1)
else:
    print(answer)