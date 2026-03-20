#Royce Daniel 3/20/2026 "Get a Class"
# START
#
# CREATE dictionary courseList with predefined course ID and course name pairs
#
# DISPLAY "Available Courses:"
# FOR each courseID in courseList
#     DISPLAY courseID and courseList[courseID]
# END FOR

# DISPLAY "How many courses would you like to take?"
# INPUT numCourses
#
# CREATE empty list called selectedCourses
#
# SET count = 0
#
# WHILE count < numCourses
#
#     DISPLAY "Enter course ID to add:"
#     INPUT choice
#
#     IF choice exists in courseList THEN
#         ADD choice to selectedCourses
#         INCREMENT count
#     ELSE
#         DISPLAY "Invalid course ID. Try again."
#     END IF
#
# END WHILE
#
# DISPLAY "Your Selected Courses:"
# FOR each courseID in selectedCourses
#     DISPLAY courseID and courseList[courseID]
# END FOR
def main():
    course_dict = {
        "COS 2005": "Python Programming",
        "COS 2100": "Data Structures",
        "MAT 1010": "College Algebra",
        "ENG 1500": "English Composition",
        "COS 2200": "Computer Organization"
    }

    print("Available Courses:")
    for course_id in course_dict:
        print(course_id, "-", course_dict[course_id])

    num_courses = int(input("\nHow many courses would you like to take? "))

    selected_courses = []

    for i in range(num_courses):
        choice = input("Enter course ID to add: ")

        if choice in course_dict:
            selected_courses.append(choice)
        else:
            print("Invalid course ID. Try again.")

            i -= 1


    print("\nYour Selected Courses:")
    for course_id in selected_courses:
        print(course_id, "-", course_dict[course_id])


main()