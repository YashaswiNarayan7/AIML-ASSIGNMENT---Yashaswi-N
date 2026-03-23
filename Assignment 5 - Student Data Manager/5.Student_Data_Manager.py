# Assignment: Student Data Manager
# Date: 19/02/2026
# Name: Yashaswi N

def calculate_grade(marks):
    """Assign grade based on marks."""
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B+"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

def main():
    print("=== Student Data Manager ===\n")

    students = {}

   
    for i in range(1, 6):
        name = input(f"Enter name of student {i}: ").strip()
        marks_input = input(f"Enter marks of {name} (0-100): ").strip()
        
  
        while not marks_input.isdigit() or int(marks_input) < 0 or int(marks_input) > 100:
            print("Please enter valid marks between 0 and 100.")
            marks_input = input(f"Enter marks of {name} (0-100): ").strip()
        marks = int(marks_input)

        students[name] = marks
        print()  

    topper_name = max(students, key=students.get)
    topper_marks = students[topper_name]


    class_average = sum(students.values()) / len(students)

    print("=== Results ===")
    print(f"Class Topper: {topper_name} with {topper_marks} marks")
    print(f"Class Average: {class_average:.2f}\n")

    print("Grades for each student:")
    for name, marks in students.items():
        grade = calculate_grade(marks)
        print(f"{name}: {marks} marks → Grade {grade}")

    input("\nPress Enter to exit...")  

if __name__ == "__main__":
    main()