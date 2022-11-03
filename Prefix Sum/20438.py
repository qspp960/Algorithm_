import sys


n, k, q, m = map(int,sys.stdin.readline().split())

sleep_student = list(map(int,sys.stdin.readline().split()))

q_student = list(map(int,sys.stdin.readline().split()))

prefix_sum = [0] * (n+3)

check_student = [0] * (n+3)

for i in range(len(q_student)):
    j = 1
    check = q_student[i]
    if check not in sleep_student:
        while (check*j) <= (n+2):
            if (check*j) not in sleep_student:
                check_student[check*j] = 1
            j += 1

for i in range(3,n+3):
    if check_student[i] == 0:
        prefix_sum[i] = prefix_sum[i-1] + 1
    else:
        prefix_sum[i] = prefix_sum[i-1]

for i in range(m):
    start, end = map(int,sys.stdin.readline().split())
    print(prefix_sum[end] - prefix_sum[start-1])

