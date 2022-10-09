import itertools

n = int(input())
k = int(input())

number = []
for i in range(n):
    num = input()
    number.append(num)

per_number = itertools.permutations(number,k)
result = []
for per in per_number:
    check_number = ""
    for p in per:
        check_number += p
    if check_number not in result:
        result.append(check_number)
print(len(result))
