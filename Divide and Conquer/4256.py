import sys

t = int(sys.stdin.readline())


def solution(left,right,root):

    for i in range(left,right):
        if preOrder[root] == inOrder[i]:
            solution(left,i,root+1)
            solution(i+1,right,root+i+1-left)

            print(preOrder[root])


while t > 0:
    n = int(sys.stdin.readline())
    preOrder = list(map(int,sys.stdin.readline().split()))
    inOrder = list(map(int,sys.stdin.readline().split()))

    solution(0,n,0)

    t -= 1

