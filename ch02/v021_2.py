student_attendance = {"Ralf": 96, "Bob": 80, "Anne": 100}

print(list(student_attendance.items()))  # List of tuples

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}%")
