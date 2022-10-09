import sys

dx = [-1,1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,-1,1,1,-1]

n = int(sys.stdin.readline())

ground_str = []
ground_result = []

for i in range(n):
    gr = list(map(str,sys.stdin.readline()))
    ground_str.append(gr)

for i in range(n):
    result = []
    for j in range(n):
        if ground_str[i][j] == '*':
            result.append('*')
        else:
            count = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if ground_str[nx][ny] == '*':
                        count += 1
            result.append(str(count))
    ground_result.append(result)

result = []
check = False
for i in range(n):
    open = sys.stdin.readline()
    result_i = []
    for j in range(n):
        if open[j] == 'x' and ground_result[i][j] == '*':
            result_i.append('*')
            check = True
        elif open[j] == 'x':
            result_i.append(ground_result[i][j])
        elif open[j] == '.':
            result_i.append('.')
    result.append(result_i)

if check:
    for i in range(n):
        for j in range(n):
            if ground_result[i][j] == '*':
                result[i][j] = '*'
for rst in result:
    print(''.join(rst))


