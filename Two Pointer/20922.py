import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())

number = list(map(int,sys.stdin.readline().split()))

if n == 1:
    print(1)
    exit(0)

end_p = 1
n_dic = {}
result = deque()
result.append(number[0])
answer = []
n_dic[number[0]] = 1

for i in range(n):
    start_p = i

    while end_p < n:
        if number[end_p] in n_dic:
            if n_dic[number[end_p]] == k:
                break
            else:
                n_dic[number[end_p]] += 1
                result.append(number[end_p])
                answer.append(len(result))
        else:
            n_dic[number[end_p]] = 1
            result.append(number[end_p])
            answer.append(len(result))
        end_p += 1

    n_dic[number[start_p]] -= 1
    result.popleft()

print(max(answer))

