n = int(input())


start = 0
end = n

while start <= end:
    middle = (start+end) // 2
    if (middle ** 2) >= n:
        end = middle - 1
    else:
        start = middle + 1
print(start)