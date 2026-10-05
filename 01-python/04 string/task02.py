"""🟡 Set 2 — Basic String Methods

Focus: upper(), lower(), strip(), replace()

Task 1

Convert this string to uppercase:

text = "python programming"
Task 2

Convert this string to lowercase:

text = "PYTHON PROGRAMMING"
Task 3

Remove the extra spaces:

text = "   Python   "
Task 4

Replace "Java" with "Python":

text = "I am learning Java"
Task 5 ⭐

Given:

text = "   PYTHON PROGRAMMING   "

Perform both:

Remove extra spaces
Convert to lowercase

Expected:

python programming"""
text = "python programming"
print(text.upper())
text = "PYTHON PROGRAMMING"
print(text.lower())
text = "   Python   "
print(text.strip())
text = "I am learning Java"
print(text.replace("Java","python"))
text = "   PYTHON PROGRAMMING   "
text=text.strip()
print(text)
text=text.lower()
print(text)



