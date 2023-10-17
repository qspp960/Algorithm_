import sys

na,nb = map(int,sys.stdin.readline().split())

a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

a_set = set(a)
b_set = set(b)

a_set = a_set.difference(b)
b_set = b_set.difference(a)

print(len(a_set) + len(b_set))