"""
🔵 Set 4 — Checking Strings

Focus: startswith(), endswith(), in, not in

Task 1

Check whether:

text = "Python Programming"

starts with "Python".

Task 2

Check whether:

text = "Python Programming"

ends with "Programming".

Task 3

Check whether "Python" exists in:

text = "I am learning Python"
Task 4

Check whether "Java" does not exist in:

text = "I am learning Python"
Task 5 ⭐

Given:

filename = "machine_learning.py"

Check:

Does it start with "machine"?
Does it end with ".py"?
Does "learning" exist in the filename?
"""
text = "Python Programming"
print(text.startswith("Python"))
text = "Python Programming"
print(text.endswith("Programming"))
text = "I am learning Python"
print("learning" in text)
text = "I am learning Python"
print("java" not in text)
filename = "machine_learning.py"
print(filename.startswith(filename))
print(filename.endswith(filename))
print("learning " in filename)
