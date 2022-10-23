k = int(input())

tree_height = [[] for _ in range(k)]

visit_order = list(map(int,input().split()))


def find_tree_height(start,end,height):
    if start == end:
        tree_height[height].append(visit_order[start])
        return

    middle = (start+end) // 2
    tree_height[height].append(visit_order[middle])
    find_tree_height(start,middle-1,height+1)
    find_tree_height(middle+1,end,height+1)


find_tree_height(0,len(visit_order)-1,0)
for t in tree_height:
    print(' '.join(map(str,t)))
