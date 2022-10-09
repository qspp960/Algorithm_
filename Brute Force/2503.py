import itertools

n = int(input())
number = [str(i) for i in range(1,10)]
permutation_number = list(itertools.permutations(number,3))

strike_ball = []
for i in range(n):
    a = list(map(str,input().split()))
    strike_ball.append(a)
result = []

for num in permutation_number:
    check = ''.join(num)
    count = 0
    for i in range(n):
        check_number = strike_ball[i][0]
        check_strike = 0
        check_ball = 0
        for j in range(3):
            if check_number[j] in check and check_number[j] == check[j]:
                check_strike += 1
            elif check_number[j] in check and check_number[j] != check[j]:
                check_ball += 1
        if check_strike == int(strike_ball[i][1]) and check_ball == int(strike_ball[i][2]):
            count += 1
    if count == n:
        result.append(check)
print(len(result))

