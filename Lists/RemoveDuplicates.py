# Remove Duplicate Elements from a List
n = int(input("Enter the number of elements: "))
numbers = []
print("Enter the elements:")
for i in range(n):
    num = int(input())
    numbers.append(num)
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("Original List:", numbers)
print("List after removing duplicates:", unique)