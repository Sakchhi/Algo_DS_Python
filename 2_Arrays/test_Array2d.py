from Array2d_ADT import Array2D

grade_file = open('gradefile.txt', 'r')
num_students = int(grade_file.readline())
num_exams = int(grade_file.readline())

exam_grades = Array2D(num_students, num_exams)
# print(exam_grades.num_rows(), exam_grades.num_cols())

i = 0
for student in grade_file:
    grades = student.split()
    for j in range(num_exams):
        exam_grades[i, j] = int(grades[j])
    i += 1
grade_file.close()

for i in range(num_students):
    total = 0
    for j in range(num_exams):
        total += exam_grades[i, j]
    exam_avg = total/num_exams
    print("%2d: %6.2f"%(i+1, exam_avg))