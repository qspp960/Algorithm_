import sys

n,k = map(int,sys.stdin.readline().split())

l = str(sys.stdin.readline().rstrip())

check = [0 for _ in range(len(l))]
answer = 0

for i in range(len(l)):
    if l[i] == "P":
        min_h = i
        copy_k = k
        current = i
        while copy_k > 0:
            current -= 1
            copy_k -= 1
            if current < 0:
                break

            if l[current] == "H" and check[current] == 0:
                min_h = current

        copy_k = k
        current = i
        if min_h == i:
            while copy_k > 0:
                current += 1
                copy_k -= 1
                if current >= len(l):
                    break

                if l[current] == "H" and check[current] == 0:
                    min_h = current
                    break

        if min_h != i:
            answer += 1
            check[min_h] = 1

print(answer)
