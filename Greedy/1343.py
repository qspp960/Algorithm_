poly = list(input().split('.'))
chk = True
for i in range(len(poly)):
    if poly[i] != '':
        if len(poly[i]) % 2 != 0:
            print(-1)
            chk = False
            break
        else:
            if len(poly[i]) % 4 == 0:
                ans = 'AAAA' * (len(poly[i]) // 4)
                poly[i] = ans
            else:
                ans = 'AAAA' * (len(poly[i]) // 4)
                ans += 'BB' * (len(poly[i]) % 4 // 2)
                poly[i] = ans

if chk == True:
    ans = ''
    for i in range(len(poly)):
        if poly[i] == '':
            ans += '.'
        else:
            ans += poly[i]
            ans += '.'

    print(ans[:-1])