n,m = map(int,input().split())

light = list(map(int,input().split()))

for i in range(m):
    a,b,c, = map(int,input().split())

    if a == 1:
        light[b-1] = c
    elif a == 2:
        for i in range(b-1,c):
            if light[i] == 1:
                light[i] = 0
            else:
                light[i] = 1
    elif a == 3:
        light[b-1:c] = [0] * (c-b+1)

    elif a == 4:
        light[b-1:c] = [1] * (c-b+1)

light_str = list(map(str,light))
result = " ".join(light_str)

print(result)

