n = int(input())

switch = list(map(int,input().split()))

n_student = int(input())

for i in range(n_student):
    a,b = map(int,input().split())

    if a == 1:

        start = 1
        while (b * start) <= n:
            current = (b * start) - 1
            if switch[current] == 0:
                switch[current] = 1
            else:
                switch[current] = 0
            start += 1

    elif a == 2:

        low_start = b - 1
        high_start = b + 1
        if switch[b-1] == 0:
            switch[b-1] = 1
        elif switch[b-1] == 1:
            switch[b-1] = 0

        while low_start >= 1 and high_start <= n:
            if switch[low_start-1] == switch[high_start-1]:
                if switch[low_start-1] == 0:
                    switch[low_start-1] = 1
                    switch[high_start-1] = 1
                else:
                    switch[low_start-1] = 0
                    switch[high_start-1] = 0
            else:
                break
            low_start -= 1
            high_start += 1

if n <= 20:
    print(' '.join(map(str,switch)))

else:
    count = n // 20
    semi_count = n % 20
    limit = 1
    while count > 0:
        switch_limit = limit * 20
        switch_start = (limit-1) * 20
        print(' '.join(map(str,switch[switch_start:switch_limit])))
        limit += 1
        count -= 1
    if semi_count > 0:
        print(' '.join(map(str,switch[n-semi_count:n])))
