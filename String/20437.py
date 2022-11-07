
t = int(input())

for i in range(t):
    w = input()
    k = int(input())

    w_dict = {}
    w_list = []

    for j in range(len(w)):
        if w[j] in w_dict:
            w_dict[w[j]].append(j)

        else:
            w_dict[w[j]] = [j]
        if len(w_dict[w[j]]) == k and w[j] not in w_list:
            w_list.append(w[j])

    min_length = 1e9

    max_length = 0

    for word in w_list:
        start = 0
        while start < len(w_dict[word]):
            next = start + (k-1)
            if next < len(w_dict[word]):
                if min_length > (w_dict[word][next]-w_dict[word][start]+1):
                    min_length = w_dict[word][next]-w_dict[word][start]+1
            else:
                break
            if max_length < ((w_dict[word][next] - w_dict[word][start]) + 1):
                max_length = ((w_dict[word][next] - w_dict[word][start]) + 1)
            start += 1

    if max_length == 0:
        print(-1)
        continue
    else:
        answer = [min_length, max_length]
        print(" ".join(map(str,answer)))









