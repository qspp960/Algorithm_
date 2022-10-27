import sys

keyboard = {
    'q': (0,1),
    'w': (0,2),
    'e': (0,3),
    'r': (0,4),
    't': (0,5),
    'y': (0,6),
    'u': (0,7),
    'i': (0,8),
    'o': (0,9),
    'p': (0,10),
    'a': (1,1),
    's': (1,2),
    'd': (1,3),
    'f': (1,4),
    'g': (1,5),
    'h': (1,6),
    'j': (1,7),
    'k': (1,8),
    'l': (1,9),
    'z': (2,1),
    'x': (2,2),
    'c': (2,3),
    'v': (2,4),
    'b': (2,5),
    'n': (2,6),
    'm': (2,7)
}

l,r = map(str,sys.stdin.readline().split())

input_string = list(sys.stdin.readline().split())
input_string = input_string[0]

l_keyboard = "qwertasdfgzxcv"

answer = 0
for i in range(len(input_string)):
    if input_string[i] in l_keyboard:
        answer += (abs(keyboard[input_string[i]][0]-keyboard[l][0]) + abs(keyboard[input_string[i]][1]-keyboard[l][1]))
        l = input_string[i]
    else:
        answer += (abs(keyboard[input_string[i]][0]-keyboard[r][0]) + abs(keyboard[input_string[i]][1]-keyboard[r][1]))
        r = input_string[i]
    answer += 1
print(answer)



