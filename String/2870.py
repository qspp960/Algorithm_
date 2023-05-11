import sys

n = int(sys.stdin.readline())
answer = []

# 0~9 48~57
# a~z 97~122


def solve(cs):
    global answer
    o_check = False
    result = ""
    for i in range(len(cs)):
        if ord(cs[i]) == 48 and o_check == False and len(result) == 0:
            o_check = True
            continue
        elif ord(cs[i]) == 48 and len(result) > 0:
            result += cs[i]
        elif ord(cs[i]) >= 97 and ord(cs[i]) <= 122:
            if len(result) > 0:
                answer.append(int(result))
                result = ""
                o_check = False
            elif len(result) == 0 and o_check == True:
                answer.append(int("0"))
                o_check = False
        elif ord(cs[i]) >= 49 and ord(cs[i]) <= 57:
            result += cs[i]

        elif cs[i] == "\n":
            if len(result) > 0:
                answer.append(int(result))

            elif len(result) == 0 and o_check == True:
                answer.append(int("0"))


for i in range(n):
    s = str(sys.stdin.readline())
    solve(s)

answer.sort()

for i in range(len(answer)):
    print(answer[i])