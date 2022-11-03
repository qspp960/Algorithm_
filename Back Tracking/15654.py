n, m = map(int,input().split())

number = list(map(int,input().split()))
number.sort()
result = []


def btk():
    if len(result) == m:
        print(' '.join(map(str,result)))
        return

    for i in range(1,n+1):
        if len(result) == 0:
            result.append(number[i-1])
            btk()
            result.pop()
        elif number[i-1] not in result:
            result.append(number[i-1])
            btk()
            result.pop()


btk()