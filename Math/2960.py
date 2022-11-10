n, k = map(int,input().split())

number = [x for x in range(2,n+1)]
check = [0] * (n+1)
count = 0
for i in range(len(number)):
    for j in range(i,len(number)):
        if (number[j] % number[i]) == 0 and check[number[j]] == 0:
            count += 1
            check[number[j]] = 1
            if count == k:
                print(number[j])
                exit(0)
