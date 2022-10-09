n = int(input())

card = list(map(int,input().split()))
m = int(input())

number = list(map(int,input().split()))
card.sort()
result = []

for i in range(m):
    rst = 0
    check = number[i]
    start = 0
    end = len(card)-1
    while start <= end:
        middle = (start+end) // 2
        if card[middle] == check:
            rst = 1
            break
        elif card[middle] < check:
            start = middle+1
        elif card[middle] > check:
            end = middle-1
    result.append(str(rst))
print(' '.join(result))