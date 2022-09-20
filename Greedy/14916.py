n = int(input())
cnt = 0

if n == 1 or n == 3:
    cnt = -1
else:
    if (n%5) % 2 == 0:
        cnt += n // 5
        cnt += (n%5) // 2
    else:
        cnt += (n//5)-1
        n = n % 5 + 5
        cnt += n // 2

print(cnt)
