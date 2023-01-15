student_attendance = {"Ralf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}%")

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}%")

if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}%")
else:
    print("Bob isn't a student.")

attendance_avg = sum(student_attendance.values()) / len(student_attendance)
print(attendance_avg)