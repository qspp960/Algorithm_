n = int(input())

request = list(map(int,input().split()))

money = int(input())

result = 0
while True:
    temp = []
    average_money = money // len(request)
    if min(request) >= average_money:
        result = average_money
        break
    elif max(request) <= average_money:
        result = max(request)
        break
    else:
        for i in range(len(request)):
            if request[i] <= average_money:
                money -= request[i]
            else:
                temp.append(request[i])
    request = temp
print(result)