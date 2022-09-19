n = int(input())

is_on = True
check = 0
copy_n = n

while is_on:
    a = 0
    b = 0
    if n < 10:
        a = 0
        b = n
    else:
        a = n // 10
        b = n % 10
    c = a + b
    c = c % 10
    n = b * 10 + c
    check += 1
    if n == copy_n:
        break
print(check)

