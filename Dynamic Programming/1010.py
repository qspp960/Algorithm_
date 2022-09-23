import itertools

T = int(input())

for i in range(T):
    r,n = map(int,input().split())
    n_list = [0] * n
    nCr = list(itertools.combinations(n_list,r))
    print(len(nCr))
