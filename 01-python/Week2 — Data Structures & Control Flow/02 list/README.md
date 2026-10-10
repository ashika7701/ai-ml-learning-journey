Python Tuples — Complete Notes
A tuple is a built-in Python data type used to store multiple items in a single variable. Tuples are ordered and immutable, which means their elements cannot be changed after creation.
1. Tuple Creation
You can create a tuple using parentheses () with comma-separated values.
Example 1: Creating a tuple
# Tuple of integersnumbers = (10, 20, 30, 40)# Tuple of stringsnames = ("Arun", "Priya", "Kumar")# Tuple with different data typesdata = (10, "Python", 3.14, True)print(numbers)print(names)print(data)



Output:
(10, 20, 30, 40)
('Arun', 'Priya', 'Kumar')
(10, 'Python', 3.14, True)


Example 2: Creating a single-element tuple
To create a tuple with only one element, you must include a comma.
a = (10,)b = (10)print(type(a))print(type(b))



Output:
<class 'tuple'>
<class 'int'>


Remember: (10,) is a tuple, but (10) is an integer.
Example 3: Creating a tuple without parentheses
Python also allows tuples to be created without parentheses.
numbers = 10, 20, 30print(numbers)print(type(numbers))



Output:
(10, 20, 30)
<class 'tuple'>



2. Tuple Indexing
Indexing is used to access individual elements from a tuple.
Python indexing starts from 0.
Example tuple
10
Index 0

20
Index 1

30
Index 2

40
Index 3



Example 1: Positive indexing
numbers = (10, 20, 30, 40, 50)print(numbers[0])print(numbers[2])print(numbers[4])



Output:
10
30
50


Example 2: Negative indexing
Negative indexing accesses elements from the end of the tuple.
numbers = (10, 20, 30, 40, 50)print(numbers[-1])print(numbers[-2])print(numbers[-5])



Output:
50
40
10


Remember:
- tuple[0] → First element
- tuple[-1] → Last element
- tuple[-2] → Second-last element

3. Tuple Slicing
Slicing is used to access a range of elements from a tuple.
Syntax
tuple[start:stop:step]



- start — Starting index, included.
- stop — Ending index, excluded.
- step — Number of positions to skip.
Example 1: Basic slicing
numbers = (10, 20, 30, 40, 50, 60)print(numbers[1:4])print(numbers[:3])print(numbers[3:])



Output:
(20, 30, 40)
(10, 20, 30)
(40, 50, 60)


Example 2: Slicing with a step
numbers = (10, 20, 30, 40, 50, 60)print(numbers[::2])print(numbers[1::2])print(numbers[::-1])



Output:
(10, 30, 50)
(20, 40, 60)
(60, 50, 40, 30, 20, 10)


Important: Slicing creates a new tuple containing the selected elements. It does not modify the original tuple.

4. Tuple Unpacking
Tuple unpacking means assigning the elements of a tuple to multiple variables in a single statement.
Example 1: Basic unpacking
student = ("Arun", 22, "Python")name, age, course = studentprint(name)print(age)print(course)



Output:
Arun
22
Python


Here:
- name receives "Arun".
- age receives 22.
- course receives "Python".
Example 2: Swapping variables
Python allows you to swap two variables without using a temporary variable.
a = 10b = 20a, b = b, aprint(a)print(b)



Output:
20
10


Example 3: Unpacking with the * operator
The * operator collects multiple remaining elements into a list.
numbers = (10, 20, 30, 40, 50)first, *middle, last = numbersprint(first)print(middle)print(last)



Output:
10
[20, 30, 40]
50


Important: The number of variables must match the number of tuple elements unless you use * unpacking.

5. Tuple vs List
Both tuples and lists store multiple items, but they differ in how their elements can be changed.
Feature	Tuple	List
Syntax	(10, 20, 30)	[10, 20, 30]
Ordered	Yes	Yes
Mutable	No	Yes
Indexing	Supported	Supported
Slicing	Supported	Supported
Duplicate values	Allowed	Allowed
Different data types	Allowed	Allowed
Append or remove items	Not directly supported	Supported
Typical use	Fixed data	Changeable data
Example: List is mutable
numbers = [10, 20, 30]numbers[0] = 100numbers.append(40)print(numbers)



Output:
[100, 20, 30, 40]


Example: Tuple is immutable
numbers = (10, 20, 30)numbers[0] = 100print(numbers)



Output:
TypeError


The error occurs because tuple elements cannot be reassigned.
When should you use each?
- Use a tuple for fixed collections, such as RGB color values or coordinates.
- Use a list when you need to add, remove, or modify elements.

6. Important Tuple Operations
Finding the length
numbers = (10, 20, 30, 40)print(len(numbers))



Output: 4
Counting occurrences
numbers = (10, 20, 10, 30, 10)print(numbers.count(10))



Output: 3
Finding an element's index
numbers = (10, 20, 30, 40)print(numbers.index(30))



Output: 2
Checking membership
numbers = (10, 20, 30, 40)print(20 in numbers)print(50 not in numbers)



Output:
True
True


Concatenating tuples
a = (10, 20)b = (30, 40)result = a + bprint(result)



Output: (10, 20, 30, 40)
