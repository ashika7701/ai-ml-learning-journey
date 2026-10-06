"""
Task 5 — String Analyzer 🚀

Take a sentence from the user.

Perform:

Convert to uppercase
Convert to lowercase
Remove extra spaces
Find "Python"
Check whether it starts with "Python"
Check whether it ends with "."
Split into words
Join words using "-"
"""
text=input("enter the text")
print(text.lower())
print(text.upper())
print(text.strip())
print(text.find("Python"))
print(text.startswith("Python"))
print(text.endswith("."))
print(text.split())
print("-".join(text))
