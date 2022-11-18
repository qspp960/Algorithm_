import sys

n, m = map(int,sys.stdin.readline().split())

n_arr = list(map(int,sys.stdin.readline().split()))

m_arr = list(map(int,sys.stdin.readline().split()))

n_p = 0
m_p = 0
result = []

while True:
    if n_p == n and m_p == m:
        break
    elif n_p == n and m_p < m:
        result.append(m_arr[m_p])
        m_p += 1
        continue

    elif n_p < n and m_p == m:
        result.append(n_arr[n_p])
        n_p += 1
        continue
    else:
        if n_arr[n_p] < m_arr[m_p]:
            result.append(n_arr[n_p])
            n_p += 1
        else:
            result.append(m_arr[m_p])
            m_p += 1

print(' '.join(map(str,result)))

# nm_arr = n_arr + m_arr
#
# nm_arr.sort()
#
# print(' '.join(map(str,nm_arr)))
