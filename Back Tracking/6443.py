import sys

n = int(sys.stdin.readline())


def solution(voca,current):
    if len(current) == len(voca):
        print(current)
        return

    for dic in check:
        if check[dic] > 0:
            check[dic] -= 1
            current += dic
            solution(voca,current)
            check[dic] += 1
            current = current[:-1]


for i in range(n):
    v = list(map(str,sys.stdin.readline().rstrip()))
    v.sort()
    check = {}

    for j in range(len(v)):
        if v[j] in check:
            check[v[j]] += 1
        else:
            check[v[j]] = 1

    solution(v,"")
