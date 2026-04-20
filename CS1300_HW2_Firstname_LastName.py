# CS1300 HW 2
# Name: Firstname Lastname

# ----------------------------
# Problem 1: User Profile Generator
# ----------------------------

first_name = input("Enter your first name: ").title()
last_name = input("Enter your last name: ").title()
birth_year = int(input("Enter your birth year: "))
hobby = input("Enter your favorite hobby: ").title()

current_year = 2026
age = current_year - birth_year

print("=" * 36)
print("       USER PROFILE CARD       ")
print("=" * 36)
print(f"Name:    {first_name} {last_name}")
print(f"Age:     {age}")
print(f"Hobby:   {hobby}")
print("-" * 36)
print("Thank you for creating your profile!")
print("=" * 36)

# ----------------------------
# Problem 2: Text Analyzer
# ----------------------------

sentence = input("\nEnter a sentence: ")

total_chars_with_spaces = len(sentence)
total_chars_without_spaces = len(sentence.replace(" ", ""))
word_count = len(sentence.split())

vowels = "aeiou"
vowel_count = 0
for char in sentence.lower():
    if char in vowels:
        vowel_count += 1

starts_with_capital = "Yes" if sentence[:1].isupper() else "No"
ends_with_punctuation = "Yes" if sentence.endswith((".", "!", "?")) else "No"

print("\n=== TEXT ANALYZER ===")
print("--- Analysis Results ---")
print(f"Total characters (with spaces):    {total_chars_with_spaces}")
print(f"Total characters (without spaces): {total_chars_without_spaces}")
print(f"Number of words:                   {word_count}")
print(f"Number of vowels:                  {vowel_count}")
print(f"Uppercase version:                 {sentence.upper()}")
print(f"Lowercase version:                 {sentence.lower()}")
print(f"Reversed:                          {sentence[::-1]}")
print(f"Starts with capital:               {starts_with_capital}")
print(f"Ends with punctuation:             {ends_with_punctuation}")

# ----------------------------
# Bonus: Palindrome Checker
# ----------------------------

text = input("\nEnter a word or phrase to check palindrome: ")

cleaned = text.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
