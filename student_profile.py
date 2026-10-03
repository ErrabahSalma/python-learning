print("======== STUDENT PROFILE ========")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
s_hours = float(input("Enter your study hours per day: "))
s_days = int(input("How many days do you study per week? "))

s_week = s_days * s_hours

print("======== PROFILE ========")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Course: {course}")
print(f"Study hours per day: {s_hours}")
print(f"Study days per week: {s_days}")
print(f"Weekly study hours: {s_week}")
