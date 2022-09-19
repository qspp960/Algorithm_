# A 65 Z 90
import sys
import math

number = list(sys.stdin.readline().split())


answer = 0

for i,num in enumerate(number[0]):
    check = 0
    b = int(number[1])

    if num >= 'A' and num <= 'Z':
        check = ord(num) - 55
        answer += check * math.pow(b,len(number[0])-i-1)
    else:
        answer += int(num) * math.pow(b,len(number[0])-i-1)

print(int(answer))
