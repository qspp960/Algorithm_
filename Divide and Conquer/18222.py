# 점화식을 찾지 못해 요구사항따라 코딩했더니 시간초과 발생 (점화식 사용해야함)
import sys

k = int(sys.stdin.readline())

n = 0

while (2**n) <= k:
    n += 1

length_x = 2**n


def solution(length_x):
    if length_x == 1:
        return '0'
    else:
        copy_s = solution(length_x//2)
        result = ''
        for i in range(len(copy_s)):
            if copy_s[i] == '0':
                result += '1'
            else:
                result += '0'
        return copy_s + result


str_result = solution(length_x//2)
if str_result[k-(length_x//2)-1] == '0':
    print(1)
else:
    print(0)

#점화식 검색 후 알아냄

k = int(input())


def solution(n):
    if n == 1:
        return 0

    if n == 2:
        return 1

    if n % 2:
        return 1 - solution(n//2)

    else:
        return solution(n//2)


print(solution(k))



