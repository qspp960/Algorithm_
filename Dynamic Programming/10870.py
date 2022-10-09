n = int(input())

def pib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return pib(n-1)+pib(n-2)
print(pib(n))