import sys

n, m = map(int,sys.stdin.readline().split())

number = list(map(int,sys.stdin.readline().split()))
p_sum = [0] * m
p_sum[number[0] % m] = 1

for i in range(1,len(number)):
    number[i] += number[i-1]

    p_sum[number[i] % m] += 1


answer = p_sum[0]

for i in range(len(p_sum)):
    answer += p_sum[i] * (p_sum[i]-1) // 2

print(answer)
