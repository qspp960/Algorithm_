n, m = map(int,input().split())

number = list(map(int,input().split()))
result = []
number.sort()
visited = [0] * n


def btk():
    if len(result) == m:
        chk = ' '.join(map(str,result))
        if chk not in double_chk:
            double_chk[chk] = 1
            print(chk)
        return

    for i in range(n):
        if visited[i] == 0:
            if len(result) == 0:
                result.append(number[i])
                visited[i] = 1
                btk()
                visited[i] = 0
                result.pop()
            elif len(result) > 0 and number[i] >= result[-1]:
                result.append(number[i])
                visited[i] = 1
                btk()
                visited[i] = 0
                result.pop()
            else:
                continue


double_chk = {}
btk()