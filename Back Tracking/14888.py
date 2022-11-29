import sys

n = int(sys.stdin.readline())

number = list(map(int,sys.stdin.readline().split()))

op = list(map(int,sys.stdin.readline().split()))
operator = []

for i in range(len(op)):
    if i == 0 and op[i] != 0:
        for j in range(op[i]):
            operator.append("+")
    elif i == 1 and op[i] != 0:
        for j in range(op[i]):
            operator.append("-")
    elif i == 2 and op[i] != 0:
        for j in range(op[i]):
            operator.append("*")
    elif i == 3 and op[i] != 0:
        for j in range(op[i]):
            operator.append("//")
max_answer = -1e15
min_answer = 1e15
visited = [0] * (n-1)


def dfs(start,result):
    if start == n:
        global max_answer
        global min_answer
        if max_answer < result:
            max_answer = result
        if min_answer > result:
            min_answer = result
        return

    for i in range(n-1):
        if visited[i] == 0:
            if operator[i] == '+':
                visited[i] = 1
                dfs(start+1,result+number[start])
                visited[i] = 0
            elif operator[i] == '-':
                visited[i] = 1
                dfs(start + 1, result - number[start])
                visited[i] = 0
            elif operator[i] == '*':
                visited[i] = 1
                dfs(start + 1, result * number[start])
                visited[i] = 0
            else:
                if number[start] < 0 or result < 0:
                    visited[i] = 1
                    dfs(start+1,-(abs(result) // abs(number[start])))
                    visited[i]=0
                else:
                    visited[i] = 1
                    dfs(start+1,result // number[start])
                    visited[i] = 0


dfs(1,number[0])
print(max_answer)
print(min_answer)
