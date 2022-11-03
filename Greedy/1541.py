sentence = input()

if '-' not in sentence:
    result = sentence.split('+')
    answer = 0
    for num in result:
        answer += int(num)
    print(answer)

elif '-' not in sentence and '+' not in sentence:
    print(int(sentence))

elif '+' not in sentence:
    result = sentence.split('-')
    answer = int(result[0])
    for i in range(1,len(result)):
        answer -= int(result[i])
    print(answer)

else:
    result = sentence.split('-')

    for i in range(len(result)):
        check_answer = 0
        if '+' in result[i]:
            check_result = result[i].split('+')
            for check in check_result:
                check_answer += int(check)
            result[i] = str(check_answer)

    answer = int(result[0])

    for i in range(1,len(result)):
        answer -= int(result[i])
    print(answer)