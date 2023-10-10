import sys
from functools import cmp_to_key

n = int(sys.stdin.readline())

user = []

for i in range(n):
    u = list(map(str,sys.stdin.readline().split()))
    user.append(u)


def diff(a,b):
    return -1 if int(a[0]) < int(b[0]) else 1
    return -1


user.sort(key=cmp_to_key(diff))

for i in range(len(user)):
    print(user[i][0], user[i][1])

