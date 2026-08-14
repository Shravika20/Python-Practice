from collections import Counter
filename = input("Enter file name: ")
try:
    with open(filename, "r") as file:
        text = file.read().lower()
    words = text.split()
    word_count = Counter(words)
    print("\nWord Frequency:")
    for word, count in word_count.most_common():
        print(f"{word}: {count}")
except FileNotFoundError:
    print("File not found.")