import sys

n,m = map(int,sys.stdin.readline().split())

number = list(map(int,sys.stdin.readline().split()))
number = set(number)
number = list(number)
number.sort()


def back_tracking(cnt):
    if cnt == m:
        print(' '.join(map(str,b_answer)))
        return

    for i in range(len(number)):
        b_answer.append(number[i])
        back_tracking(cnt+1)
        b_answer.pop()


b_answer = []
back_tracking(0)
