"""🟠 Set 3 — Split, Join & Find

Focus: split(), join(), find()

Task 1

Convert this string into a list:

text = "Python Java C++"

Expected:

['Python', 'Java', 'C++']
Task 2

Given:

languages = ["Python", "Java", "C++"]

Join them using:

-

Expected:

Python-Java-C++
Task 3

Find the position of "Python":

text = "I love Python"
Task 4

Find the position of "Programming":

text = "Python Programming"
Task 5 ⭐

Given:

text = "Python is easy"
Split the string into words.
Join the words using " "."""
text = "Python Java C++"
text=text.split()
text=list(text)
print(text)

languages = ["Python", "Java", "C++"]
languages="-".join(languages)
print(languages)
text = "I love Python"
print(text.find("Python"))
print(text.find("programming"))
text = "Python is easy"
text=text.split()
print(text)
print(" ".join(text))
