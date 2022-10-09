T = int(input())


def solution(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return solution(n-1)+solution(n-2)+solution(n-3)


for i in range(T):
    n = int(input())
    dp = [0] * (n+1)
    print(solution(n))



