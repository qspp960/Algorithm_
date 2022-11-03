from itertools import combinations


i_string = list(input())
i_string_index = []
i_string_comb = []
answer = []
for i in range(len(i_string)):
    if i_string[i] == ')':
        i_string_index.append(i)


def make_string(check):
    copy_string = i_string.copy()

    for i in range(len(check)):
        check_index = check[i]
        count = 0
        for j in range(check_index,-1,-1):
            if check_index == j:
                copy_string[j] = '.'
                continue
            if copy_string[j] == ')':
                count += 1
                continue
            if copy_string[j] == '(':
                if count == 0:
                    copy_string[j] = '.'
                    break
                else:
                    count -= 1
    result = ''.join(copy_string)
    result = result.replace('.','')
    answer.append(result)
    return


for i in range(len(i_string_index),0,-1):
    i_string_comb.append(list(combinations(i_string_index,i)))

max_comb_length = len(i_string_comb)

for i in range(max_comb_length):
    for j in range(len(i_string_comb[i])):
        check = i_string_comb[i][j]
        make_string(check)

set_answer = set(answer)
my_answer = list(set_answer)
my_answer.sort()

for ans in my_answer:
    print(ans)