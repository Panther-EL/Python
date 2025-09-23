students = []         
no_students = int(input('How many students are there?'))
for i in range(no_students):
    name = input('Enter student name: ')
    try:
        score = int(input("Enter the student's score: "))
        if score < 0 or score > 100:
            print('Score must be within the range 0-100')#Checks for a valid range
        else:
            if score >= 90:
                remark='A'
            elif score >= 80:
                remark='B'
            elif score >= 70:
                remark='C'
            elif score >= 60:
                remark='D'
                
            else:
                remark='F'
            students.append([name,score,remark])
    except ValueError:
        print('Invalid input,your input is non-numeric')
print(students)
