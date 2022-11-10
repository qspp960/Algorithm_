t = int(input())


def gcd(a,b):
    if b % a == 0:
        return a

    return gcd(b%a,a)


for i in range(t):
    a,b = map(int,input().split())

    g = gcd(a,b)

    answer = ((a//g) * (b//g)) * g
    print(answer)