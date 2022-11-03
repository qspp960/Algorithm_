import sys

n, m = map(int,sys.stdin.readline().split())

tree = list(map(int,sys.stdin.readline().split()))

tree.sort()

start = 0
end = tree[-1]
f_result = 0

while start <= end:
    length_tree = (start + end) // 2
    result = 0

    for i in range(n):
        if tree[i] > length_tree:
            result += (tree[i] - length_tree)

    if result > m:
        start = length_tree + 1
        f_result = length_tree
    elif result == m:
        f_result = length_tree
        break
    else:
        end = length_tree - 1
        f_result = length_tree-1
print(f_result)



