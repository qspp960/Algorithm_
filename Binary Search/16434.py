import sys
import math

n, ha = map(int,sys.stdin.readline().split())
room = []
hm = 0

# 1인 경우 용, 2인 경우 포션


for i in range(n):
    r = list(map(int,sys.stdin.readline().split()))
    if r[0] == 1:
        hm += (r[1] * r[2])
    room.append(r)


def solve(h_m):
    h_c = h_m
    h_a = ha

    for i in range(n):
        if room[i][0] == 2:
            h_a += room[i][1]
            h_c += room[i][2]

            if h_c > h_m:
                h_c = h_m

        elif room[i][0] == 1:
            monster_hp = room[i][2]
            monster_a = room[i][1]
            h_count = math.ceil((h_c / monster_a))
            m_count = math.ceil((monster_hp / h_a))

            if h_count < m_count:
                return False

            h_c -= (monster_a * (m_count-1))

    return True


start = 1
end = hm

while start <= end:
    mid = (start+end) // 2

    if solve(mid) == True:
        end = mid - 1
    else:
        start = mid + 1

print(start)