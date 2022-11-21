import sys

duck = sys.stdin.readline()
duck = duck[:-1]
answer = 0
kind_duck = ['q','u','a','c','k']
visited = [0] * len(duck)
duck_count = 0
check = 0


def find_duck(kind,index):
    for i in range(index,len(duck)):

        if duck[i] == kind_duck[kind] and visited[i] == 0:
            kind += 1
            visited[i] = 1

            if kind == 5:
                global check
                check += 1
                kind = 0


for i in range(len(duck)):
    result = []
    if duck[i] == 'q' and visited[i] == 0:
        check = 0
        visited[i] = 1
        find_duck(1,i+1)

        if check > 0:
            answer += 1

if 0 in visited:
    print(-1)
    exit(0)
if answer == 0 or (len(duck) % 5) != 0:
    print(-1)
    exit(0)
print(answer)

