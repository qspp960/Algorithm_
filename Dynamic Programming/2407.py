n, m = map(int,input().split())

nr = 1
start_n = n

for i in range(m):
    nr *= start_n
    start_n -= 1

mr = 1
start_m = m

for i in range(m):
    mr *= start_m
    start_m -= 1

print(nr//mr)
