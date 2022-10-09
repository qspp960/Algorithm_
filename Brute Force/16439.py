import itertools

n, m = map(int,input().split())
chicken = []
for i in range(n):
    chic = list(map(int,input().split()))
    chicken.append(chic)

chicken_index = list(itertools.combinations([i for i in range(0,m)],3))
max_result = 0
for chic in chicken_index:
    result = 0
    for i in range(n):
        result += max(chicken[i][chic[0]],chicken[i][chic[1]],chicken[i][chic[2]])
    max_result = max(result,max_result)
print(max_result)

