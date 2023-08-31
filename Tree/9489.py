import sys
import copy

while True:
    n,k = map(int,sys.stdin.readline().split())
    if n == 0 and k == 0:
        break

    node = list(map(int,sys.stdin.readline().split()))
    if len(node) < 2:
        print(0)
        continue

    k_p = -1
    number = []
    number.append([node[0]])
    check = []
    check.append(node[1])
    for i in range(2,len(node)):
        if check[-1] == (node[i]-1):
            check.append(node[i])
        else:
            check_copy = copy.deepcopy(check)
            number.append(check_copy)
            check.clear()
            check.append(node[i])

        if i == (len(node)-1):
            number.append(check)

    if len(number) <= 2:
        print(0)
        continue

    dict = {
        str(number[0][0]): number[1]
    }

    for i in range(len(number[1])):
        dict[str(number[1][i])] = []

    for i in range(2,len(number)):
        for parent, child in dict.items():
            if len(child) == 0:
                dict[parent] = number[i]
                if k in number[i]:
                    k_p = int(parent)
                break

        for j in range(len(number[i])):
            dict[str(number[i][j])] = []

    answer = 0

    for parent, child in dict.items():
        if k_p in child:
            for i in range(len(child)):
                if child[i] != k_p:
                    answer += len(dict[str(child[i])])

    print(answer)



