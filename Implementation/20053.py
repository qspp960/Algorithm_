t = int(input())


for i in range(t):
    n = int(input())
    number = list(map(int,input().split()))

    number.sort()
    print(f"{number[0]} {number[-1]}")
