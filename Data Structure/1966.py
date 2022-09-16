

T = int(input())

for i in range(T):
    answer = 0
    paper, find = map(int,input().split())
    queue = list(input().split())
    check = [0] * paper
    check[find] = 1

    while True:
        if queue[0] == max(queue) and check[0] == 1:
            answer += 1
            break
        elif queue[0] == max(queue):
            del queue[0]
            del check[0]
            answer += 1
        else:
            queue.append(queue[0])
            check.append(check[0])
            del queue[0]
            del check[0]
    print(answer)








