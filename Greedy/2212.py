import sys

n = int(sys.stdin.readline())

k = int(sys.stdin.readline())

sensor = list(map(int,sys.stdin.readline().split()))

sensor.sort()

btw_sensor = []

for i in range(len(sensor)-1):
    btw_sensor.append(sensor[i+1]-sensor[i])

btw_sensor.sort()
answer = sum(btw_sensor[:len(btw_sensor)-k+1])
print(answer)