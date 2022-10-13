n,r,c = map(int,input().split())

dx = [0,0,1,1]
dy = [0,1,0,1]
result = []


def solution(x,y,size,number):

    if size == 2:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            number += 1
            if nx == r and ny == c:
                result.append(number-1)
                return
        return

    upper_left_x = x
    upper_left_y = y
    upper_left_number = number

    upper_right_x = x
    upper_right_y = y + (size//2)
    upper_right_number = number + (((size//2)**2)*1)

    lower_left_x = x + (size//2)
    lower_left_y = y
    lower_left_number = number + (((size//2)**2)*2)

    lower_right_x = x + (size//2)
    lower_right_y = y + (size//2)
    lower_right_number = number + (((size//2)**2)*3)

    if upper_left_x <= r <= upper_left_x+(size//2)-1 and upper_left_y <= c <= upper_left_y + (size//2)-1:
        solution(upper_left_x,upper_left_y,size//2,upper_left_number)
    elif upper_right_x <= r <= upper_right_x+(size//2)-1 and upper_right_y <= c <= upper_right_y + (size//2)-1:
        solution(upper_right_x, upper_right_y, size // 2, upper_right_number)
    elif lower_left_x <= r <= lower_left_x+(size//2)-1 and lower_left_y <= c <= lower_left_y + (size//2)-1:
        solution(lower_left_x, lower_left_y, size // 2, lower_left_number)
    elif lower_right_x <= r <= lower_right_x+(size//2)-1 and lower_right_y <= c <= lower_right_y + (size//2)-1:
        solution(lower_right_x, lower_right_y, size // 2, lower_right_number)


solution(0,0,2**n,0)
print(result[0])


