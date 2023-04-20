import sys

s = str(sys.stdin.readline().rstrip())

t = str(sys.stdin.readline().rstrip())

answer = False

if s == t:
    print(1)
    exit(0)

current = t


def change(current):
    if current == s:
        global answer
        answer = True
        return

    if len(current) == 0:
        return

    if current[-1] == "A":
        change(current[:len(current)-1])

    if current[0] == "B":
        current = current[1:]
        change(current[::-1])


change(t)
if answer == True:
    print(1)
else:
    print(0)

