import sys

stc = str(sys.stdin.readline())
stc = stc[:-1]

dic = {}

for i in range(len(stc)):
    current = ord(stc[i])

    if current > 90:
        current -= 32

    current = str(current)

    if current in dic:
        dic[current] += 1

    else:
        dic[current] = 1

max_v = 0
answer = ""
check = 0
for item in dic.items():
    if max_v < item[1]:
        max_v = item[1]
        answer = chr(int(item[0]))
        check = 0

    elif max_v == item[1]:
        check = 1

if check == 1:
    print("?")
else:
    print(answer)
