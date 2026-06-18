n = int(input("Enter number of students: "))
students = {}
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
print("\nStudent Records:")
for name, marks in students.items():
    print(name, ":", marks)