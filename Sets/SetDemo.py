n = int(input("How many elements do you want to enter? "))
my_set = set()
for i in range(n):
    value = input(f"Enter element {i+1}: ")
    my_set.add(value)
print("Set:", my_set)
print("Number of unique elements:", len(my_set))