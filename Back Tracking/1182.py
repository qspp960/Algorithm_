import sys

n, s = map(int,sys.stdin.readline().split())

number = list(map(int,sys.stdin.readline().split()))


def back_tracking(current):
    if len(answer) != 0 and sum(answer) == s:
        global result
        result += 1

    for i in range(current+1,n):
        answer.append(number[i])
        back_tracking(i)
        answer.pop()


result = 0
answer = []
back_tracking(-1)
print(result)
