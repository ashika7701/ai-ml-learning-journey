"""
🔵 Level 4 — Sorting & Nested Lists

Task 11: Model Scores

You have the following model scores:

[0.82, 0.91, 0.76, 0.95, 0.88]
Arrange them from smallest to largest.
Arrange them from largest to smallest.
Display the final list after each operation"""
list1=[0.82, 0.91, 0.76, 0.95, 0.88]
list1.sort()
print(list1)
list1=list1[::-1]
print(list1)
"""Task 12: Student Dataset

Create a nested list containing information for 4 students.

Each student should have:

Name
Age
Mark

Example structure:

[
    [...],
    [...],
    [...],
    [...]
]

Then:

Display the first student's information.
Display the second student's name.
Display the third student's mark."""


print("marks",student_details[2][1])
"""

Task 13: ML Dataset

Create this dataset:

[
    [25, 50000, 2],
    [30, 60000, 4],
    [35, 75000, 7],
    [28, 55000, 3]
]

Treat each inner list as:

[age, salary, experience]

Display:

All ages.
The salary of the third person.
The experience of the second person.
The complete data of the fourth person."""

dataset=[
    [25, 50000, 2],
    [30, 60000, 4],
    [35, 75000, 7],
    [28, 55000, 3]
]

print(dataset[0][0])
print(dataset[2][1])
print(dataset[1][2])
print(dataset[3])
"""
🔴 Level 5 — User Input

Task 14: User-Defined Dataset

Ask the user how many values they want to enter.

Take the values from the user and store them in a list.

After collecting all values:

Display the list.
Display the values in ascending order.
Display the values in descending order.
"""
dataset=[]
n=int(input("enter how many value have"))
for i in range(n):
  values=input("enter values")
  if values.isdigit():
    values=int(values)
  dataset.append(values)
for valuees in dataset:
  print(valuees)
dataset.sort()
print(dataset)
dataset.reverse()
print(dataset)
"""
Task 15: Prediction Analysis

Ask the user to enter the number of predictions.

Then collect the predictions one by one.

After collecting them, display:

All predictions.
Number of 1 predictions.
Number of 0 predictions.
Position of the first 1.
Position of the first 0
"""
dataset=[]
n=int(input("enter how much data to store"))
for i in range(n):
  values=int(input("enter valuees"))
  dataset.append(values)
print(dataset.count(1))
print(dataset.count(0))
first1=dataset.index(1)
print(first1)
first0=dataset.index(0)
print(first0)
