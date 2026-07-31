# Store and Display Student Marks using Dictionary
students = {}
n = int(input("Enter the number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
print("\nStudent Details")
for name, marks in students.items():
    print(name, ":", marks)
highest = max(students, key=students.get)
print("\nTop Scorer")
print(highest, ":", students[highest])