n = int(input())

quad_tree = []

for i in range(n):
    quad = input()
    quad_tree.append(quad)

result = []


def solution(x,y,size):
    cnt = 0
    for i in range(x,x+size):
        for j in range(y,y+size):
            cnt += int(quad_tree[i][j])
    if cnt == 0:
        result.append('0')
        return
    elif cnt == (size*size):
        result.append('1')
        return

    else:
        middle = size // 2
        result.append('(')
        solution(x,y,middle)
        solution(x,y+middle,middle)
        solution(x + middle, y, middle)
        solution(x+middle,y+middle,middle)
        result.append(')')


solution(0,0,n)
print(''.join(result))

