🐍 Python — str and None

Professional Learning Notes
Clear explanations • Separate programs • GitHub-friendly Markdown

1. str — String

str stands for String. It is a Python data type used to store text.

A string is a sequence of characters enclosed inside quotes.

name = "Python"
city = 'Chennai'

Both single quotes (' ') and double quotes (" ") can be used.

1.1 Creating a String

Program

name = "John"
course = "Python"
message = "Hello World"

print(name)
print(course)
print(message)

Output

John
Python
Hello World

Checking the Data Type

name = "John"

print(type(name))

Output

<class 'str'>

1.2 Single Quotes vs Double Quotes

Both are valid ways to create a string:

name1 = "Python"
name2 = 'Python'

print(name1)
print(name2)

Output

Python
Python

Both produce the same string value.

1.3 Characters Allowed in a String

A string can contain:

Letters

Numbers

Spaces

Special characters

Program

a = "Python"
b = "12345"
c = "Python 3"
d = "Hello @123!"

print(a)
print(b)
print(c)
print(d)

Important: "12345" is a string, not an integer.

x = "12345"

print(type(x))

Output

<class 'str'>

int vs str

a = 123
b = "123"

print(type(a))
print(type(b))

Output

<class 'int'>
<class 'str'>

2. Multi-line Strings

Python allows strings to span multiple lines using triple quotes.

Program

message = """Hello
Welcome to Python
Let's learn programming"""

print(message)

Output

Hello
Welcome to Python
Let's learn programming

You can use either:

""" """

or:



for multi-line strings.

3. String Indexing

Each character in a string has an index.

Python uses zero-based indexing, which means the first character has index 0.

For:

name = "Python"

the positions are:

Character :  P   y   t   h   o   n
Index     :  0   1   2   3   4   5

Accessing Characters

name = "Python"

print(name[0])
print(name[1])
print(name[5])

Output

P
y
n

3.1 Negative Indexing

Python also supports negative indexing.

Character :  P   y   t   h   o   n
Index     : -6  -5  -4  -3  -2  -1

Program

name = "Python"

print(name[-1])
print(name[-2])

Output

n
o

Remember: -1 refers to the last character.

4. String Slicing

Slicing is used to get a part of a string.

Syntax

string[start:stop]

The stop index is not included.

Example

name = "Python"

print(name[0:3])

Output

Pyt

The indexes are:

Python
012345

So name[0:3] takes indexes 0, 1, and 2.

4.1 More Slicing Examples

name = "Python"

print(name[:3])
print(name[2:])
print(name[:])

Output

Pyt
thon
Python

5. String Length — len()

Use the len() function to find the number of characters in a string.

Program

name = "Python"

print(len(name))

Output

6

Spaces are also counted.

message = "Hello World"

print(len(message))

Output

11

6. String Concatenation

Concatenation means joining strings together.

The + operator is used for concatenation.

Program

first_name = "John"
last_name = "David"

full_name = first_name + " " + last_name

print(full_name)

Output

John David

7. String Repetition

You can repeat a string using the * operator.

Program

message = "Hi "

print(message * 3)

Output

Hi Hi Hi

8. String Methods

Python provides many built-in string methods.

8.1 upper()

Converts a string to uppercase.

name = "python"

print(name.upper())

Output

PYTHON

8.2 lower()

Converts a string to lowercase.

name = "PYTHON"

print(name.lower())

Output

python

8.3 strip()

Removes spaces from the beginning and end of a string.

name = "  Python  "

print(name.strip())

Output

Python

8.4 replace()

Replaces part of a string with another value.

message = "I like Java"

print(message.replace("Java", "Python"))

Output

I like Python

8.5 split()

Splits a string into a list.

text = "Python is easy"

print(text.split())

Output

['Python', 'is', 'easy']

9. Strings Are Immutable

Immutable means a string cannot be changed after it is created.

For example:

name = "Python"

# name[0] = "J"

The above modification causes an error because an individual character of a string cannot be changed directly.

Instead, create a new string:

name = "Python"

name = "J" + name[1:]

print(name)

Output

Jython

Key concept: Strings are immutable.

10. Converting to String — str()

Use str() to convert a value into a string.

Program

age = 25

age_text = str(age)

print(age_text)
print(type(age_text))

Output

25
<class 'str'>

This is especially useful when combining numbers and text.

age = 25

print("My age is " + str(age))

Output

My age is 25

11. f-Strings

f-strings provide a convenient way to insert variables into strings.

Program

name = "John"
age = 25

message = f"My name is {name} and I am {age} years old."

print(message)

Output

My name is John and I am 25 years old.

Note: f-strings are frequently used in Python programs.

12. None in Python

None is a special value in Python that represents the absence of a value or no value.

Its data type is called NoneType.

Program

x = None

print(x)
print(type(x))

Output

None
<class 'NoneType'>

12.1 What Does None Mean?

Think of None as:

"There is currently no value here."

Example

result = None

print(result)

Output

None

None is different from:

result = 0

Here, 0 is an actual integer value.

It is also different from:

result = ""

Here, "" is an empty string.

Comparison

Value

Meaning

None

No value

0

Integer value

""

Empty string

False

Boolean value

13. None and NoneType

The type of None is NoneType.

Program

x = None

print(type(x))

Output

<class 'NoneType'>

There is one special None object in normal Python code, written as:

None

14. Assigning None to a Variable

You can assign None to a variable when you do not have a value yet.

name = None

print(name)

Later, you can assign an actual value:

name = None

name = "John"

print(name)

Output

John

15. None as a Function Return Value

A function that does not explicitly return a value returns None.

Program

def greet():
    print("Hello")

result = greet()

print(result)

Output

Hello
None

Why?

The function prints "Hello", but it does not have a return statement.

Therefore, Python automatically returns None.

16. return None

You can explicitly return None from a function.

Program

def check_age(age):
    if age < 18:
        return None

result = check_age(15)

print(result)

Output

None

A bare return also returns None:

def check_age(age):
    if age < 18:
        return

17. Checking for None

The recommended way to check whether a value is None is to use is.

Check for None

name = None

if name is None:
    print("No name provided")

Output

No name provided

Check that a value is not None

name = "John"

if name is not None:
    print("Name is available")

Output

Name is available

Preferred Style

Use:

if x is None:

instead of:

if x == None:

Best practice: Use is None and is not None when checking for None.

18. None vs False

None and False are different values.

a = None
b = False

print(a == b)

Output

False

Their types are also different:

print(type(a))
print(type(b))

Output

<class 'NoneType'>
<class 'bool'>

19. None vs 0

None is not the same as 0.

a = None
b = 0

print(a == b)

Output

False

Remember:

None → No value
0    → Integer value

20. None is Falsy

None is considered falsy in a Boolean context.

Program

x = None

if x:
    print("True")
else:
    print("False")

Output

False

Important: None being falsy does not mean None is equal to False.

print(None == False)

Output

False

21. Common Uses of None

None is often used to indicate that a value is not available yet.

username = None
email = None
phone = None

Later, values can be assigned:

username = "John"
email = "john@example.com"

None is commonly encountered in real-world programs, APIs, databases, and machine-learning code.

📌 Quick Revision

str

Concept

Example

Data type

str

Create string

"Python"

Indexing

name[0]

Negative indexing

name[-1]

Slicing

name[0:3]

Length

len(name)

Concatenation

"Hello" + "World"

Repetition

"Hi " * 3

Uppercase

.upper()

Lowercase

.lower()

Remove spaces

.strip()

Replace text

.replace()

Split text

.split()

Convert to string

str(25)

Most Important str Points

str → String → Text

Python
   ↓
String
   ↓
Characters
   ↓
Indexing / Slicing / Methods

Remember: Strings are ordered, indexable, sliceable, and immutable sequences of characters.

None

Value

Meaning

Type

None

No value

NoneType

0

Zero

int

""

Empty string

str

False

False

bool

Important Syntax

x = None

Check for None:

if x is None:
    print("No value")

Check that a value is not None:

if x is not None:
    print("Value exists")
