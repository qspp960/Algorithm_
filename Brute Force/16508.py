import sys
from itertools import combinations

book = []
price = []
comb = []
answer = 1e9
check_answer = False

t = sys.stdin.readline().split()[0]

n = int(input())


for i in range(n):
    p,b = map(str,sys.stdin.readline().split())

    price.append(int(p))
    book.append(b)
    comb.append(i)

for i in range(1,n+1):
    c_book = list(combinations(comb,i))

    for j in range(len(c_book)):
        sum_str = {}
        sum_cost = 0
        for k in range(len(c_book[j])):
            sum_cost += price[c_book[j][k]]

            for m in range(len(book[c_book[j][k]])):
                current_chr = book[c_book[j][k]][m]
                if current_chr in sum_str:
                    sum_str[current_chr] += 1
                else:
                    sum_str[current_chr] = 1
        check_str = True
        for s in range(len(t)):
            if t[s] in sum_str and sum_str[t[s]] > 0:
                sum_str[t[s]] -= 1
            else:
                check_str = False
                break

        if check_str == True:
            check_answer = True
            answer = min(answer,sum_cost)


if check_answer == False:
    print(-1)
else:
    print(answer)







