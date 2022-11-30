import sys

n = int(sys.stdin.readline())
answer = 0

for i in range(n):
    s = sys.stdin.readline()
    sen = s[:-1]
    s_dic = {}

    for j in range(len(sen)):
        if sen[j] not in s_dic:
            s_dic[sen[j]] = 1

        else:
            if sen[j-1] != sen[j]:
                s_dic[sen[j]] = 0
            else:
                continue
    check = True

    for d in s_dic:
        if s_dic[d] == 0:
            check = False
            break

    if check == True:
        answer += 1

print(answer)

