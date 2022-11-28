import sys

n = int(sys.stdin.readline())
egg = []
answer = 0

for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))

    egg.append(a)


def dfs(current):
    if current == n:
        count = 0
        for i in range(n):
            if egg[i][0] <= 0:
                count += 1

        global answer
        if answer < count:
            answer = count
        return

    if egg[current][0] <= 0:
        dfs(current+1)
    else:
        check = True
        for i in range(n):

            if i == current:
                continue
            if egg[i][0] <= 0:
                continue
            if egg[i][0] > 0:
                check = False
                egg[current][0] -= egg[i][1]
                egg[i][0] -= egg[current][1]

                dfs(current+1)

                egg[current][0] += egg[i][1]
                egg[i][0] += egg[current][1]
        if check == True:
            dfs(current+1)

dfs(0)

print(answer)