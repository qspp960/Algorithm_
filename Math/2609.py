import sys
a, b = map(int,sys.stdin.readline().split())


def gcd(a,b):
    if a == 0:
        return b
    else:
        return gcd(b%a,a)


ans1 = gcd(a,b)
ans2 = a*b//ans1   #몰랐다
print(ans1)
print(ans2)