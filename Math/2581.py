m = int(input())
n = int(input())

prime_number = [i for i in range(n+1)]
prime_number[1] = 0

for i in range(2,n+1):
    if prime_number[i] == 0:
        continue

    for j in range(i+1,n+1):
        if (j % i) == 0:
            prime_number[j] = 0

result = []

for i in range(m,n+1):
    if prime_number[i] != 0:
        result.append(prime_number[i])

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(result[0])
