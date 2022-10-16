import sys

n = int(sys.stdin.readline())
file = {}

for i in range(n):
    f = sys.stdin.readline()

    check_dot = 0
    f_name = ''
    for j in range(len(f)):
        if f[j] == '.':
            check_dot = 1
            continue
        if check_dot == 1:
            f_name += f[j]

    if f_name in file:
        file[f_name] += 1
    else:
        file[f_name] = 1

s_file = sorted(file.items())

for f in s_file:
    key = f[0].split()
    value = str(f[1])
    print(f"{key[0]} {value}")


