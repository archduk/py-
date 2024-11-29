#lists of students and their grades
students = ['Alice', 'Brian', 'Ellyvis']
grades = [85, 90, 98]

#Using zip() to loop through both lists simultaneously
for student, grade in zip(students, grades):
    print(f"Student: {student}, Grade: {grade}")
