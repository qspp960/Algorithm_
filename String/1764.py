import sys

n,m = map(int,sys.stdin.readline().split())
n_set = set()
m_set = set()
answer = []
cnt = 0
for i in range(n):
    s = sys.stdin.readline()
    s = s[:-1]
    n_set.add(s)

for j in range(m):
    s = sys.stdin.readline()
    s = s[:-1]
    m_set.add(s)

answer = list(n_set&m_set)
print(len(answer))
answer.sort()
for i in range(len(answer)):
    print(answer[i])