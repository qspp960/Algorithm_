import sys
import math

t = int(sys.stdin.readline())


def solve(h,w,n):
    w_f = math.ceil(n / h)
    h_f = n % h

    if h_f == 0:
        h_f = h

    if w_f < 10:
        answer = str(h_f) + "0" + str(w_f)
    else:
        answer = str(h_f) + str(w_f)

    print(answer)


for i in range(t):
    h,w,n = map(int,sys.stdin.readline().split())
    solve(h,w,n)