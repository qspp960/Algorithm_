import sys

n, k = map(int,sys.stdin.readline().split())

number = list(map(int,sys.stdin.readline().split()))

answer = 0
prefix_sum = {}
p_sum = 0

for i in range(n):
    p_sum += number[i]

    if p_sum == k:
        answer += 1

    check = p_sum - k
    if str(check) in prefix_sum:
        answer += prefix_sum[str(check)]

    if str(p_sum) in prefix_sum:
        prefix_sum[str(p_sum)] += 1
    else:
        prefix_sum[str(p_sum)] = 1

print(answer)


