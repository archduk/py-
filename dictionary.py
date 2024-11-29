# Function to invert the dictionary
def invert_dictionary(student_courses):
    # Create an empty dictionary to store the inverted result
    course_students = {}

    # Iterate over each student and their list of courses
    for student, courses in student_courses.items():
        for course in courses:
            # If the course is not already a key in the inverted dictionary, add it
            if course not in course_students:
                course_students[course] = []
            # Add the student to the list of students for that course
            course_students[course].append(student)

    return course_students

# Original dictionary with students and their courses
student_courses = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}

# Invert the dictionary
inverted_dict = invert_dictionary(student_courses)

# Print the original dictionary
print("Original Dictionary:")
print(student_courses)

# Print the inverted dictionary
print("\nInverted Dictionary:")
print(inverted_dict)
