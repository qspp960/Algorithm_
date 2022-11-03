n,m = map(int,input().split())

result = []

def btk(start):
    if len(result) == m:
        print(' '.join(map(str,result)))
        return

    for i in range(start,n):
        if (i + 1) not in result:
            result.append(i+1)
            btk(i)
            result.pop()
btk(0)