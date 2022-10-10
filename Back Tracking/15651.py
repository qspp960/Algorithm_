n, m = map(int,input().split())

result = []


def btk():
    if len(result) == m:
        print(' '.join(map(str,result)))
        return

    for i in range(n):
        result.append(i+1)
        btk()
        result.pop()

btk()
