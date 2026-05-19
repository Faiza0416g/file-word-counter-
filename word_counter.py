from collections import Counter

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        text = file.read().lower()

        words = text.split()

        word_count = Counter(words)

        print("\nWord Occurrences:\n")

        for word, count in sorted(word_count.items()):
            print(f"{word}: {count}")

except FileNotFoundError:
    print("File not found. Please check the file name.")
