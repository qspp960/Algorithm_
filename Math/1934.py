t = int(input())


def gcd(a,b):
    if (a % b) == 0:
        return b
    elif (b % a) == 0:
        return a
    return gcd(b,a%b)


for i in range(t):
    a,b = map(int,input().split())

    answer = (a*b) // gcd(a,b)
    print(answer)



