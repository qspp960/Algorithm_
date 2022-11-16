import sys

n, k = map(int,sys.stdin.readline().split())

number = list(map(int,sys.stdin.readline().split()))
answer = 0
max_answer = 0
count = 0
pointer = 0
# 투포인터!!!!!


for i in range(n):

    while count <= k and pointer < n:
        if number[pointer] % 2 != 0:
            count += 1
            pointer += 1

        else:
            pointer += 1
            answer += 1

    if max_answer < answer:
        max_answer = answer

    if number[i] % 2 != 0:
        count -= 1
    else:
        answer -= 1


print(max_answer)





