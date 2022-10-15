t = int(input())
check_s_e = ['A','B','C','D','E','F']

for i in range(t):
    test_string = str(input())
    check_a = False
    check_f = False
    check_c = False
    check_end = 0
    check = True
    length = len(test_string)

    for k in range(length):
        if k == 0:
            if test_string[k] == 'A':
                check_a = True
            elif test_string[k] not in check_s_e:
                check = False
                break
            elif test_string[k] in check_s_e:
                if test_string[k+1] != 'A':
                    check = False
                    break
                else:
                    check_a = True
        else:

            if check_a == True:
                if test_string[k] == 'A':
                    continue
                elif test_string[k] == 'F':
                    check_a = False
                    check_f = True
                    continue
                else:
                    check = False
                    break
            elif check_f == True:
                if test_string[k] == 'F':
                    continue
                elif test_string[k] == 'C':
                    check_f = False
                    check_c = True
                    continue
                else:
                    check = False
                    break

            elif check_c == True:
                if test_string[k] == 'C':
                    continue
                elif test_string[k] in check_s_e:
                    if k != (length-1):
                        check = False
                        break
                else:
                    check = False
                    break
    if check == False:
        print("Good")

    else :
        print("Infected!")