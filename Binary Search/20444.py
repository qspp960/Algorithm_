import sys

n,k = map(int,sys.stdin.readline().split())


#가로방향 n/2 세로방향 n/2 로 자르는게 색종이가 가장 많이나온다
#그래서 가로방향을 기준으로 이분탐색 시작 0과 n/2
answer = False
start = 0
end = n // 2

while start <= end:
    #mid는 가로방향으로 자른 횟수
    mid = (start + end) // 2

    paper = (mid + 1) * (n - mid + 1)

    if paper == k:
        answer = True
        break

    elif paper > k:
        end = mid - 1
    else:
        start = mid + 1

if answer == True:
    print("YES")
else:
    print("NO")

