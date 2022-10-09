import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n = int(sys.stdin.readline())
desk = [[0]*(n+1) for _ in range(n+1)]
students = {}

for i in range(1,n**2+1):
    student = list(map(int,sys.stdin.readline().split()))
    students[student[0]] = student[1:]

    max_j = 0
    max_k = 0
    max_love = -1
    max_blank = -1
    for j in range(1,n+1):
        for k in range(1,n+1):
            if desk[j][k] == 0:
                new_love = 0
                new_blank = 0
                for m in range(4):
                    nx = j + dx[m]
                    ny = k + dy[m]
                    if 1 <= nx <= n and 1 <= ny <= n:
                        if desk[nx][ny] in student:
                            new_love += 1
                        if desk[nx][ny] == 0:
                            new_blank += 1
                if max_love < new_love or (max_love == new_love and new_blank > max_blank):
                    max_j = j
                    max_k = k
                    max_love = new_love
                    max_blank = new_blank
    desk[max_j][max_k] = student[0]

love_count = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        count = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 1 <= nx <= n and 1 <= ny <= n:
                if desk[nx][ny] in students[desk[i][j]]:
                    count += 1
        if count != 0:
            love_count += (10**(count-1))
print(love_count)