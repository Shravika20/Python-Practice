numbers = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    value = int(input("Enter element: "))
    numbers.append(value)
key = int(input("Enter the element to search: "))
found = False
for i in range(len(numbers)):
    if numbers[i] == key:
        print("Element found at position", i + 1)
        found = True
        break
if not found:
    print("Element not found")