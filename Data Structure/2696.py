import sys

t = int(sys.stdin.readline())


for i in range(t):
    k = int(sys.stdin.readline())

    if k <= 10:
        number = list(map(int,sys.stdin.readline().split()))
        s_number = []
        answer= []
        for s in range(len(number)):
            if ((s+1) % 2) != 0:
                s_number.append(number[s])
                s_number.sort()
                answer.append(s_number[len(s_number) // 2])
            else:
                s_number.append(number[s])
        print(len(answer))
        print(" ".join(map(str,answer)))

    else:
        number = []
        if (k % 10) == 0:
            i_k = k // 10
        else:
            i_k = (k // 10) + 1
        for j in range(i_k):
            k_number = list(map(int,sys.stdin.readline().split()))
            number += k_number

        s_number = []
        answer = []
        for s in range(len(number)):
            if ((s + 1) % 2) != 0:
                s_number.append(number[s])
                s_number.sort()
                answer.append(s_number[len(s_number) // 2])
            else:
                s_number.append(number[s])

        if len(answer) > 10:
            if len(answer) % 10 == 0:
                a_k = len(answer) // 10
            else:
                a_k = len(answer) // 10 + 1
            print(len(answer))
            for s in range(a_k):
                if s == (a_k-1):
                    print(" ".join(map(str,answer[s*10:])))
                else:
                    print(" ".join(map(str,answer[s*10:(s+1)*10])))
        else:
            print(len(answer))
            print(" ".join(map(str,answer)))

