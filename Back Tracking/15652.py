n, m = map(int,input().split())

result = []

def btk():

    if len(result) == m:
        print(' '.join(map(str,result)))
        return

    for i in range(n):
        if result and result[-1] <= (i+1):
            result.append(i+1)
            btk()
            result.pop()
        elif result and result[-1] > (i+1):
            continue
        else:
            result.append(i+1)
            btk()
            result.pop()
btk()
