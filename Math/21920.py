import sys

n = int(sys.stdin.readline())

number = list(map(int,sys.stdin.readline().split()))

x = int(sys.stdin.readline())


def gcd(a,b):
    if b % a == 0:
        return a
    return gcd(b%a,a)


result = 0
count = 0

for i in range(n):
    if gcd(x,number[i]) == 1:
        result += number[i]
        count += 1

print(result/count)
