n = int(input())

number = list(map(int,input().split()))

max_number = max(number)
prime_number = [i for i in range(max_number+1)]
prime_number[1] = 0

for i in range(2,max_number+1):
    if prime_number[i] == 0:
        continue

    for j in range(i+1,max_number+1):
        if (j % i) == 0:
            prime_number[j] = 0

answer = 0

for i in range(len(number)):
    if prime_number[number[i]] != 0:
        answer += 1

print(answer)
