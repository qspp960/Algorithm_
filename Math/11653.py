n = int(input())

if n == 1:
    exit(0)

number = [x for x in range(2,n+1)]
result = []

while n != 1:
    for i in range(len(number)):
        if (n % number[i]) == 0:
            n /= number[i]
            result.append(number[i])
            break

for i in range(len(result)):
    print(result[i])