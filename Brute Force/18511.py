from itertools import product

n, k = map(int,input().split())

list_k = list(map(str,input().split()))
length = len(str(n))

while True:
    product_list = list(product(list_k,repeat=length))
    result = []
    for temp in product_list:
        check = int(''.join(temp))
        if check <= n:
            result.append(check)
    if len(result) >= 1:
        print(max(result))
        break
    else:
        length -= 1





