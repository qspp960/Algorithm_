import sys

r,c,k = map(int,sys.stdin.readline().split())
board = []
for i in range(3):
    b = list(map(int,sys.stdin.readline().split()))
    board.append(b)


timer = 0
answer = -1


def rs(select,board):
    new_board = []
    max_length = 0

    for i in range(len(board)):
        result = []
        for j in range(len(board[i])):

            if board[i][j] == 0:
                continue

            check = False

            for m in range(len(result)):
                if result[m][0] == board[i][j]:
                    check = True
                    result[m][1] += 1
                    break
            if check == False:
                result.append([board[i][j],1])
        result.sort(key=lambda x: (x[1],x[0]))
        new_result = []
        for j in range(len(result)):
            new_result.append(result[j][0])
            new_result.append(result[j][1])

        new_board.append(new_result)
        max_length = max(max_length,len(new_result))

    for i in range(len(new_board)):
        new_board[i] += ([0] * (max_length-len(new_board[i])))

        if len(new_board[i]) > 100:
            new_board[i] = new_board[i][:100]

    if select == 'r':
        return new_board
    else:
        return [list(row) for row in zip(*new_board)]


while True:

    if timer >= 101:
        break

    if 0 < r <= len(board) and 0 < c <= len(board[0]) and board[r-1][c-1] == k:
        answer = timer
        break


    if len(board) >= len(board[0]):
        board = rs('r',board)

    else:
        board = rs("c",[list(row) for row in zip(*board)])

    timer += 1

print(answer)
