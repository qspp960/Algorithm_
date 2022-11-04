import sys

n, m = map(int,sys.stdin.readline().split())

number = list(map(int,sys.stdin.readline().split()))

number = set(number)
number = list(number)
number.sort()


def back_tracking(current,cnt):

    if cnt == m:
        print(' '.join(map(str,answer)))
        return

    for i in range(current,len(number)):
        answer.append(number[i])
        back_tracking(i,cnt+1)
        answer.pop()


answer = []
back_tracking(0,0)