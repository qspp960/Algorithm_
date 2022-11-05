n = int(input())


def start(k):
    if k == 1:
        return ["*"]

    star = start(k//3)
    result = []

    for s in star:
        result.append(s*3)
    for s in star:
        result.append(s+" " * (k//3) + s)
    for s in star:
        result.append(s*3)

    return result


print('\n'.join(start(n)))
