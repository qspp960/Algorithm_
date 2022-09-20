n = int(input())
rope = []

for i in range(n):
    k = int(input())
    rope.append(k)
rope.sort(reverse=True)

answer = 0

for j in range(len(rope)):
    answer = max(rope[j] * (j+1),answer)

print(answer)

