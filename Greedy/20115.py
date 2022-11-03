n = int(input())

drink = list(map(int,input().split()))

max_drink = max(drink)

sum_drink = (sum(drink) - max_drink) / 2

print('%0.5f'%(max_drink+sum_drink))

