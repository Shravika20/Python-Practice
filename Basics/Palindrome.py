text = input("Enter a string: ")

reversed_text = text[::-1]

if text == reversed_text:
    print("Palindrome")
else:
    print("Not a Palindrome")