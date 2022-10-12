n = int(input())

paper = []
paper_dict = {
    '0': 0,
    '1': 0,
}

for i in range(n):
    p = list(map(int,input().split()))
    paper.append(p)


def solution(x,y,size):
    start_x = x
    start_y = y
    sum = 0
    for i in range(start_x,(start_x+size)):
        for j in range(start_y,(start_y+size)):
            sum += paper[i][j]
    if sum == (size*size):
        paper_dict['1'] += 1
        return
    elif sum == 0:
        paper_dict['0'] += 1
        return
    middle = size // 2
    solution(x,y,middle)
    solution(x,y+middle,middle)
    solution(x+middle,y,middle)
    solution(x+middle,y+middle,middle)


solution(0,0,n)
print(paper_dict['0'])
print(paper_dict['1'])


