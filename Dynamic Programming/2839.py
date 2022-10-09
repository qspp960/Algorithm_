n = int(input())
answer = 0

if n % 5 == 0:
    answer = n // 5
else:
    cnt = 0
    while n >= 0:
        n -= 3
        cnt += 1
        if n % 5 == 0:
            answer = (n//5) + cnt
            break
        elif n == 1 or n == 2:
            answer = -1
            break
print(answer)



