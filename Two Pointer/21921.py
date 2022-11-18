import sys

n, x = map(int,sys.stdin.readline().split())

visit = list(map(int,sys.stdin.readline().split()))
result = []
sum_visit = 0
start_p = 0
end_p = (x-1)
for i in range(x):
    sum_visit += visit[i]
    result.append(sum_visit)
while end_p < n-1:
    start_p += 1
    end_p += 1

    sum_visit -= visit[start_p-1]
    sum_visit += visit[end_p]

    result.append(sum_visit)

answer = max(result)

if answer == 0:
    print("SAD")
    exit(0)

if x == n:
    print(sum(visit))
    exit(0)

count = 0
for i in range(len(result)):
    if answer == result[i]:
        count += 1
print(answer)
print(count)