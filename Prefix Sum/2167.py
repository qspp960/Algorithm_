n,m = map(int,input().split())

number = []

for i in range(n):
    num = list(map(int,input().split()))
    number.append(num)

k = int(input())


for m in range(k):
    i,j,x,y = map(int,input().split())
    i -= 1
    j -= 1
    x -= 1
    y -= 1
    result = 0

    if i == x:
        for s in range(j,y+1):
            result += number[i][s]
    elif j == y:
        for s in range(i,x+1):
            result += number[s][j]
    else:
        for s in range(i,x+1):
            for v in range(j,y+1):
                result += number[s][v]

    print(result)

