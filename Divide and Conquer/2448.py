n = int(input())

start = (n // 3)


def star(st):
    if st == 1:
        stars = []
        stars.append("*")
        stars.append("* *")
        stars.append("*****")
        return stars

    stars = star(st//2)
    result = []

    for s in stars:
        result.append(s)

    empty = len(result[-1])

    for s in stars:
        result.append(s + " " * empty + s)
        empty -= 2

    return result


answer = star(start)

block = (start * 5) + (start-1)

for i in range(len(answer)):
    empty = block - len(answer[i])
    empty //= 2
    print(" " * empty + answer[i] + " " * empty)

