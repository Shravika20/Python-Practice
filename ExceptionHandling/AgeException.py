age = int(input("Enter your age: "))
try:
    if age < 18:
        raise Exception("You are not eligible to vote.")
    print("You are eligible to vote.")
except Exception as e:
    print(e)