import sys
from itertools import combinations

t = int(sys.stdin.readline())


def gcd(a,b):
    if b % a == 0:
        return a
    return gcd(b%a,a)


for i in range(t):
    n = list(map(int,sys.stdin.readline().split()))
    length = n[0]
    number = n[1:]
    answer = 0
    cb_number = combinations(number,2)

    for cb in cb_number:
        answer += gcd(cb[0],cb[1])

    print(answer)


