import sys

subject = []
for i in range(20):
    s = list(map(str,sys.stdin.readline().split()))
    subject.append(s)

count = 0
result = 0
for i in range(len(subject)):
    score = subject[i][2]
    sbj = float(subject[i][1])

    if score == "A+":
        score = 4.5
    elif score == "A0":
        score = 4.0
    elif score == "B+":
        score = 3.5
    elif score == "B0":
        score = 3.0
    elif score == "C+":
        score = 2.5
    elif score == "C0":
        score = 2.0
    elif score == "D+":
        score = 1.5
    elif score == "D0":
        score = 1.0
    elif score == "F":
        score = 0
    elif score == "P":
        continue

    count += sbj
    result += (sbj * score)

answer = result / count
print(round(answer,6))

