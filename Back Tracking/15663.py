n, m = map(int,input().split())

number = list(map(int,input().split()))
number.sort()

visited = [0] * 8
result = []



def btk():
    if len(result) == m:
        chk = ' '.join(map(str,result))
        if chk not in double_check:
            double_check[chk] = 1
            print(chk)
            return
        else:
            return

    for i in range(n):
        if len(result) == 0:
            visited[i] = 1
            result.append(number[i])
            btk()
            visited[i] = 0
            result.pop()
        elif visited[i] == 0:
            visited[i] = 1
            result.append(number[i])
            btk()
            visited[i] = 0
            result.pop()


double_check = {}


btk()

