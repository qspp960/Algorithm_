import sys

t = int(sys.stdin.readline())
p_check = [0] * 11


def btk(g_player,current):
    if len(g_player) == 11:
        global answer
        answer = max(answer,sum(g_player))
        return

    for j in range(11):
        if p_check[j] == 1 or player[current][j] == 0:
            continue

        if p_check[j] == 0:
            p_check[j] = 1
            g_player.append(player[current][j])
            btk(g_player,current+1)
            p_check[j] = 0
            g_player.pop()


while t > 0:
    player = []
    answer = 0
    for i in range(11):
        player.append(list(map(int, sys.stdin.readline().split())))

    gp = []
    btk(gp,0)
    t -= 1
    print(answer)
