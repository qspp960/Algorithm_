import sys

n = int(sys.stdin.readline())

w = list(map(int,sys.stdin.readline().split()))

w.sort()

left = 0
right = len(w)-1
r_left = 0
r_right = len(w)-1
answer = 1e10
check = 0

while left < right:
    mix = w[left] + w[right]
    if abs(answer) > abs(mix):
        r_left = w[left]
        r_right = w[right]
        answer = mix
    if mix > 0:
        right -= 1
    elif mix < 0:
        left += 1
    elif mix == 0:
        break

result = [r_left,r_right]
print(' '.join(map(str,result)))