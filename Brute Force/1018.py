import sys

n,m = map(int,sys.stdin.readline().split())
w_chess = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
b_chess = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]

ch = []
answer = 1e10
for i in range(n):
    c = str(sys.stdin.readline().rstrip())
    ch.append(c)


def solve(i,j):
    w_count = 0
    b_count = 0
    c_i = 0
    c_j = 0
    x = i
    y = j
    for i in range(x,x+8):
        for j in range(y,y+8):
            if ch[i][j] != w_chess[c_i][c_j]:
                w_count += 1
            if ch[i][j] != b_chess[c_i][c_j]:
                b_count += 1
            c_j += 1
        c_j = 0
        c_i += 1
    return min(w_count,b_count)


for i in range(n-7):
    for j in range(m-7):
        answer = min(answer,solve(i,j))

print(answer)


