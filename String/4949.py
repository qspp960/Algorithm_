import sys


def check_stc(cstc):
    stack = []

    for i in range(len(cstc)):
        if len(stack) == 0:
            if cstc[i] == ")" or cstc[i] == "]":
                return False

        if cstc[i] == "(" or cstc[i] == "[":
            stack.append(cstc[i])

        elif cstc[i] == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif cstc[i] == "]":
            if stack[-1] == "[":
                stack.pop()
            else:
                return False

    if len(stack) != 0:
        return False
    return True


while True:
    stc = str(sys.stdin.readline())
    stc = stc[:-1]
    if stc == ".":
        break
    if check_stc(stc) == True:
        print("yes")
        continue
    print("no")
