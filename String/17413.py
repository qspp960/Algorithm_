import sys

input_str = sys.stdin.readline()

tag_check = False
word = ''
result = ''

for i in range(len(input_str)):
    check = input_str[i]

    if check == '<':
        tag_check = True
        result += word[::-1]
        result += '<'
        word = ''
        continue

    elif check == '>':
        tag_check = False
        result += '>'
        continue

    if tag_check == True:
        result += check

    elif tag_check == False and check != ' ':
        word += check
        if i == (len(input_str) - 2):
            result += word[::-1]

    elif tag_check == False and check == ' ':
        result += word[::-1]
        result += ' '
        word = ''
print(result)


