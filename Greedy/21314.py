import sys

m_number = sys.stdin.readline()
max_result = []
max_number = ""
min_result = []
min_number = ""

for i in range(len(m_number)):
    if m_number[i] == 'M':
        max_number += 'M'

        min_number += "M"

    elif m_number[i] == 'K':
        max_number += 'K'
        max_result.append(max_number)
        max_number = ""

        if min_number != "":
            min_result.append(min_number)
            min_result.append("K")
            min_number = ""
        else:
            min_result.append("K")

if max_number != "":
    max_result.append(max_number)

if min_number != "":
    min_result.append(min_number)

max_answer = ""
min_answer = ""

for i in range(len(max_result)):
    m = 0
    k = 0
    for j in range(len(max_result[i])):
        if max_result[i][j] == 'M':
            m += 1
        else:
            k += 1

    if k == 0:
        max_answer += str('1'* m)
    else:
        max_answer += str((10 ** m) * 5)

for i in range(len(min_result)):
    m = 0
    k = 0
    for j in range(len(min_result[i])):
        if min_result[i][j] == 'M':
            m += 1
        else:
            k += 1

    if m > 0:
        min_answer += str(10**(m-1))
    else:
        min_answer += str(5)

print(max_answer)
print(min_answer)

