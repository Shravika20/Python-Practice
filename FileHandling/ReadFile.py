try:
    file = open("student.txt", "r")
    data = file.read()
    print("File Content:")
    print(data)
    file.close()
except FileNotFoundError:
    print("File does not exist.")