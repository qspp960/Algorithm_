n = int(input())
km = list(map(int,input().split()))
oil = list(map(int,input().split()))

sum_cost = 0
low_oil = oil[0]
for i in range(n-1):
    low_oil = min(low_oil,oil[i])
    new_cost = low_oil * km[i]
    sum_cost += new_cost
print(sum_cost)
