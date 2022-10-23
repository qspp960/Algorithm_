import sys

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]


def check_cut_vertex(node):
    if len(tree[node]) <= 1:
        return True

    return False


for i in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

q = int(sys.stdin.readline())

for i in range(q):
    t, k = map(int,sys.stdin.readline().split())

    if t == 1:
        if check_cut_vertex(k):
            print("no")
        else:
            print("yes")

    else:
        print("yes")








