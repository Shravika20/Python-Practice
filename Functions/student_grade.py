def calculate_total(marks):
    return sum(marks)
def calculate_average(total, subjects):
    return total / subjects
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"
# Taking user input
marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)
# Calculations
total = calculate_total(marks)
average = calculate_average(total, 5)
grade = calculate_grade(average)
# Display result
print("\n--- Student Result ---")
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)