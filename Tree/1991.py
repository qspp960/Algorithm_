n = int(input())

tree = {}
preorder = []
inorder = []
postorder = []


def preorder_traversal(current_root):
    preorder.append(current_root)
    if tree[current_root][0] != '.':
        preorder_traversal(tree[current_root][0])

    if tree[current_root][1] != '.':
        preorder_traversal(tree[current_root][1])


def inorder_traversal(current_root):

    if tree[current_root][0] != '.':
        inorder_traversal(tree[current_root][0])

    inorder.append(current_root)

    if tree[current_root][1] != '.':
        inorder_traversal(tree[current_root][1])


def postorder_traversal(current_node):
    if tree[current_node][0] != '.':
        postorder_traversal(tree[current_node][0])

    if tree[current_node][1] != '.':
        postorder_traversal(tree[current_node][1])

    postorder.append(current_node)


for i in range(n):
    root, left, right = map(str,input().split())

    tree[root] = [left,right]

preorder_traversal('A')
inorder_traversal('A')
postorder_traversal('A')

print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))