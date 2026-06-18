n = int(input("How many elements do you want in the tuple? "))
elements = []
for i in range(n):
    value = input(f"Enter element {i+1}: ")
    elements.append(value)
my_tuple = tuple(elements)
print("Tuple:", my_tuple)
print("Number of elements:", len(my_tuple))