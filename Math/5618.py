import sys


def gcd(a,b):
    if a == 0:
        return b
    else:
        return gcd(b%a,a)


n = int(input())
answer = []

number = list(map(int,sys.stdin.readline().split()))
common = gcd(number[0],gcd(number[1],number[-1]))

for i in range(1,common//2+1):
    if common % i == 0:
        print(i)
print(common)







