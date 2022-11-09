import sys

trees = {}
count = 0

while True:
    tree = sys.stdin.readline().rstrip()

    if not tree:
        break
    count += 1

    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

tree = sorted(trees.items())

for i in range(len(tree)):
    print('{0} {1:0.4f}'.format(tree[i][0],(tree[i][1]*100)/count))



