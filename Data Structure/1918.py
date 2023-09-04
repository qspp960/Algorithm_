import sys

sentence = str(sys.stdin.readline())
sentence = sentence[:-1]

stack = []
answer = ""

for i in range(len(sentence)):
    current = sentence[i]
    if current == "(":
        stack.append(current)

    elif current == ")":
        while stack:
            c_current = stack.pop()
            if c_current == "(":
                break
            answer += c_current
    elif current == "*" or current == "/":
        while len(stack) != 0 and (stack[-1] == "*" or stack[-1] == "/"):
            if stack[-1] == "(":
                break
            answer += stack.pop()
        stack.append(current)

    elif current == "+" or current == "-":
        while len(stack) != 0 and (stack[-1] == "*" or stack[-1] == "/" or stack[-1] == "+" or stack[-1] == "-"):
            if stack[-1] == "(":
                break
            answer += stack.pop()
        stack.append(current)

    else:
        answer += current

while stack:
    answer += stack.pop()

print(answer)




