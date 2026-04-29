def mark_attendance():
    student_name = input("Enter student name:")
    attendance_status = input("Enter attendance (Present/Absent):").lower()

    if attendance_status == "present":
        return student_name, 1
    elif attendance_status == "absent":
       return student_name, 0
    else:
        print("Invalid input. Marked as absent.")
        return student_name, 0


def calculate_percentage(present_count, student_count):
    if present_count == 0:
        return 0
    return (total_present/student_count) * 100

student = []
total_present = 0

while True:
    name, present = mark_attendance()
    student.append((name, present))
    total_present += present

    choice = input("Add another student? (yes/no): ").lower()
    if choice != "yes":
        break


print("\n--- Attendance Report ---")
for student in student:
    status ="Present" if student[1] == 1 else "Absent"
    print(student[0], "-", status)

percentage = calculate_percentage(total_present, len(student))

print("\nTotal Students: ", len(student))
print("Total Present: ", total_present)
print("Attendance Percentage:", percentage, "%")


