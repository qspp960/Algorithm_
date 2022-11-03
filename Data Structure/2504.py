
i_string = list(input())
dq = []
check_answer = True
check_string = []


def check():
    for i in range(len(i_string)):
        if i_string[i] == '(' or i_string[i] == '[':
            check_string.append(i_string[i])
        elif i_string[i] == ')':
            if not check_string or check_string[-1] != '(':
                print(0)
                exit(0)
            else:
                check_string.pop()
        elif i_string[i] == ']':
            if not check_string or check_string[-1] != '[':
                print(0)
                exit(0)
            else:
                check_string.pop()
        else:
            print(0)
            exit(0)

def solution():
    global check_answer
    for i in range(len(i_string)):

        if i_string[i] == ')':
            count = 0
            while len(dq) != 0:
                top = dq.pop()

                if top == '(':
                    if count == 0:
                        dq.append(2)
                    else:
                        dq.append(count*2)
                    break
                elif top == '[' or top == ']' or top == ')':
                    check_answer = False
                    break
                else:
                    count = count + int(top)


        elif i_string[i] == ']':
            count = 0
            while len(dq) != 0:
                top = dq.pop()

                if top == '[':
                    if count == 0:
                        dq.append(3)
                    else:
                        dq.append(count*3)
                    break
                elif top == '(' or top == ')' or top == ']':
                    check_answer = False
                    break
                else:
                    count = count + int(top)
        elif i_string[i] == '(' or i_string[i] == '[':
            dq.append(i_string[i])
    return

check()
solution()

result = 0
if check_answer == False:
    print(0)
    exit(0)

for i in dq:
    if i == '(' or i == '[':
        print(0)
        exit(0)
    else:
        result += i
print(result)

