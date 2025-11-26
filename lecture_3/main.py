def get_user_input():
    # Show menu and ask user to choose an option
    while True:
        print("--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")

        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Please enter a valid choice (from 1 to 5)")
        except ValueError:
            print("Please enter a valid choice (from 1 to 5)")

def add_student():
    # Add a new student with empty grades
    print("Enter student name:")
    name = input()
    student = {"name": name, "grades": []}
    return student

def add_grades(students):
    # Add grades for an existing student
    print("Enter student name:")
    name = input()
    for student in students:
        if student["name"] == name:
            while True:
                grade_input = input("Enter a grade (or 'done' to finish): ")
                if grade_input == "done":
                    break
                try:
                    grade = int(grade_input)
                    if 0 <= grade <= 100:
                        student["grades"].append(grade)
                    else:
                        print ("Please enter a valid grade (from 0 to 100)")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            return
    print(f"A student with the name {name} can't be found")

def show_report(students):
    # Show average grades for all students
    print("--- Student Report ---")
    if not students:
        print("No students found")
        return

    avg_grades = []

    for student in students:
            name = student["name"]
            grades = student["grades"]
            try:
                avg_grade = sum(grades) / len(grades)
                print(f"{name}'s average grade is {avg_grade}.")
                avg_grades.append(avg_grade)
            except ZeroDivisionError:
                print(f"{name}'s average grade is N/A.")

    if not avg_grades:
        print("No grades found")
        return

    # Show overall statistics
    max_avg_grade = max(avg_grades)
    min_avg_grade = min(avg_grades)
    overall_avg_grade = sum(avg_grades) / len(avg_grades)
    print("------------------------")
    print(f"Max Average: {max_avg_grade}")
    print(f"Min Average: {min_avg_grade}")
    print(f"Overall Average: {overall_avg_grade}")

def find_top_performer(students):
    # Find student with the highest average grade
    if not students:
        print("No students found")
        return

    students_with_grades = [student for student in students if student["grades"]]
    if not students_with_grades:
        print("No students with grades found")
        return

    top_performer = max(students_with_grades, key=lambda student: sum(student["grades"]) / (len(student["grades"])))
    top_performer_avg_grade = sum(top_performer["grades"]) / len(top_performer["grades"])
    print(f"The student with the highest average is {top_performer['name']} with a grade of {top_performer_avg_grade}.")

def main():
    students = []
    while True:
        choice = get_user_input()
        if choice == 1:
            student = add_student()
            students.append(student)
        elif choice == 2:
            add_grades(students)
        elif choice == 3:
            show_report(students)
        elif choice == 4:
            find_top_performer(students)
        elif choice == 5:
            print("Exiting program.")
            break



if __name__ == "__main__":
    main()