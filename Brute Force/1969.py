import operator

n,m = map(int,input().split())

dna = []
result = ''

for i in range(n):
    da = input()
    dna.append(da)


for j in range(m):
    check_dna = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0,
    }
    count = 0
    for i in range(n):
        check_dna[dna[i][j]] += 1
    result += max(check_dna,key=check_dna.get)
result_distance = 0
for i in range(n):
    count = 0
    for j in range(m):
        if result[j] != dna[i][j]:
            count += 1
    result_distance += count
print(result)
print(result_distance)
