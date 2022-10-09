
students = []
for i in range(28):
    student = int(input())
    students.append(student)

not_students = []
for i in range(1,31):
    if i not in students:
        not_students.append(i)

not_students.sort()
print(not_students[0])
print(not_students[1])