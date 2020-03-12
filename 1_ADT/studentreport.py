from studentfile import StudentFileReader

FILE_NAME = "students.txt"

def main():
    reader = StudentFileReader(FILE_NAME)
    reader.open()
    student_list = reader.fetch_all()
    reader.close()
    print(student_list)

    student_list.sort(key=lambda rec: rec.id)
    print_report(student_list)


def print_report(stu_list):
    class_names = (None, 'Freshman', 'Sophomore', 'Junior', 'Senior')

    print("LIST OF STUDENTS".center(50))
    print('')
    print('%-5s %-25s %-10s %-4s'%('ID', 'NAME', 'CLASS', 'GPA'))
    print('%-5s %-25s %-10s %-4s'%('-'*5, '-'*25, '-'*10, '-'*4))

    for record in stu_list:
        print('%-5d %-25s %-10s %-4.2f'%(
            record.id,
            record.last_name + ', ' + record.first_name,
            class_names[record.class_code],
            record.gpa
        ))
    print('-'*50)
    print('Number of students: ', len(stu_list))


main()