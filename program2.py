#program4- Interactive Command-Line Task Scheduler with Lazy Evaluation

import string

text = input("Enter a sentence or text: ")

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Remove extra spaces and convert to lowercase
words = text.lower().split()

# Total word count
total_words = len(words)

# Frequency of each word
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Find palindrome words
palindromes = []

for word in words:
    if len(word) > 1 and word == word[::-1]:
        if word not in palindromes:
            palindromes.append(word)

# Display results
print("\n--- Text Analysis Report ---")
print("Total words:", total_words)

print("\nWord Frequency:")
for word, count in frequency.items():
    print(word, ":", count)

print("\nPalindrome words:")
if palindromes:
    print(", ".join(palindromes))
else:
    print("No palindrome found.")