import sys

# - 최종상태
# X 승리시
# X 가 O보다 1많아야함 그리고 빙고

# O 승리시
# X와 O의 숫자가 같아야함 그리고 빙고

# 빙고가 없고 빈칸이 없을때


def bingo_check(t):
    x_check = False
    o_check = False

    d_count = 0
    x_count = 0
    o_count = 0
    for i in range(len(t)):
        if t[i] == "O":
            o_count += 1
        elif t[i] == "X":
            x_count += 1
        elif t[i] == ".":
            d_count += 1

    if o_count > x_count:
        print("invalid")
        return
    elif (x_count - o_count) > 1 or (x_count - o_count) < 0:
        print("invalid")
        return


    tt = []
    tt.append(t[:3])
    tt.append(t[3:6])
    tt.append(t[6:9])

    for i in range(3):
        for j in range(3):
            if tt[i][j] == "X":
                #가로
                l_y = j - 1
                r_y = j + 1
                if l_y >= 0 and l_y < 3 and r_y >= 0 and r_y < 3:
                    if tt[i][l_y] == "X" and tt[i][r_y] == "X":
                        x_check = True
                #세로
                u_x = i - 1
                d_x = i + 1
                if u_x >= 0 and u_x < 3 and d_x >= 0 and d_x < 3:
                    if tt[u_x][j] == "X" and tt[d_x][j] == "X":
                        x_check = True
                #대각선
                l_x = i - 1
                l_y = j - 1

                r_x = i + 1
                r_y = j + 1

                if l_x >= 0 and l_x < 3 and l_y >= 0 and l_y < 3 and r_x >= 0 and r_x < 3 and r_y >= 0 and r_y < 3:
                    if tt[l_x][l_y] == "X" and tt[r_x][r_y] == "X":
                        x_check = True

                r_x = i - 1
                r_y = j + 1

                l_x = i + 1
                l_y = j - 1

                if l_x >= 0 and l_x < 3 and l_y >= 0 and l_y < 3 and r_x >= 0 and r_x < 3 and r_y >= 0 and r_y < 3:
                    if tt[l_x][l_y] == "X" and tt[r_x][r_y] == "X":
                        x_check = True

            if tt[i][j] == "O":
                # 가로
                l_y = j - 1
                r_y = j + 1
                if l_y >= 0 and l_y < 3 and r_y >= 0 and r_y < 3:
                    if tt[i][l_y] == "O" and tt[i][r_y] == "O":
                        o_check = True
                # 세로
                u_x = i - 1
                d_x = i + 1
                if u_x >= 0 and u_x < 3 and d_x >= 0 and d_x < 3:
                    if tt[u_x][j] == "O" and tt[d_x][j] == "O":
                        o_check = True
                # 대각선
                l_x = i - 1
                l_y = j - 1

                r_x = i + 1
                r_y = j + 1

                if l_x >= 0 and l_x < 3 and l_y >= 0 and l_y < 3 and r_x >= 0 and r_x < 3 and r_y >= 0 and r_y < 3:
                    if tt[l_x][l_y] == "O" and tt[r_x][r_y] == "O":
                        o_check = True

                r_x = i - 1
                r_y = j + 1

                l_x = i + 1
                l_y = j - 1

                if l_x >= 0 and l_x < 3 and l_y >= 0 and l_y < 3 and r_x >= 0 and r_x < 3 and r_y >= 0 and r_y < 3:
                    if tt[l_x][l_y] == "O" and tt[r_x][r_y] == "O":
                        o_check = True

    if x_check == True and o_check == True:
        print("invalid")
        return

    if x_check == True:
        if (x_count - 1) == o_count:
            print("valid")
            return


    if o_check == True:
        if x_count == o_count:
            print("valid")
            return

    if x_check == False and o_check == False:
        if d_count == 0:
            print("valid")
            return

    print("invalid")
    return


while True:
    t = str(sys.stdin.readline())
    if t[:3] == "end":
        break
    bingo_check(t)


