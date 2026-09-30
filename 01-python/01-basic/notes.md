Python Fundamentals

Beginner-friendly notes for learning Python and preparing for AI/ML
development.

Table of Contents

Python Installation

Python Interpreter

Interpreter vs Interpreted
Language

Compiler and Bytecode

IDE vs Code Editor

Running Python Files

Comments

Docstrings

Indentation

Variables

Naming Conventions

Input and Output

Interview Quick Revision

1. Python Installation

If you are learning Python for AI/ML, install Python 3 and use VS Code
as your editor.

Download Python

Download Python from the official website:

https://www.python.org/downloads/

For Windows, download the Windows installer (64-bit).

Install Python

During installation:

Run the installer.

Check:

Add python.exe to PATH

Click Install Now.

Verify Python Installation

Open Command Prompt:

Win + R → cmd → Enter

Check the Python version:

python --version

Example:

Python 3.x.x

Check pip:

pip --version

pip is Python's package installer.

Test Python

Run:

python

You should see:

Python 3.x.x ...
>>>

Then:

print("Hello, Python!")

Output:

Hello, Python!

Exit the Python interpreter:

exit()

VS Code

Download VS Code:

https://code.visualstudio.com/

After installation, install the Python extension from Microsoft.

2. Python Interpreter

A Python interpreter is a program/runtime that reads and executes
Python code.

Conceptually:

Python Code
    ↓
Python Interpreter / Runtime
    ↓
Execution
    ↓
Output

Example:

print("Hello World")

Output:

Hello World

Interactive Python Interpreter

After installing Python, run:

python

You will see:

>>>

This is the Python interactive prompt.

You can directly execute Python code:

>>> 10 + 20
30

>>> print("Python")
Python

This interactive environment is called the REPL:

R → Read
E → Evaluate
P → Print
L → Loop

Exit with:

>>> exit()

Interactive Interpreter vs Python File

Interactive

>>> print("Hello")
Hello

Useful for quickly testing small pieces of code.

Python File

Create:

hello.py

Add:

print("Hello")

Run:

python hello.py

3. Interpreter vs Interpreted Language

These two terms are related but different.

Interpreter

An interpreter is software that executes a program.

Interpreter = software/program

Interpreted Language

An interpreted language is a classification commonly used for a
language whose programs are typically executed through a
runtime/interpreter rather than being compiled directly to native
machine code ahead of execution.

Interpreted language = language classification

Important: Saying that an interpreted language executes source code
strictly "line by line" is an oversimplification. Modern
implementations may use bytecode, caching, JIT compilation, and other
optimizations.

4. Compiler and Bytecode

Python is commonly described as an interpreted language, but Python
implementations can have a compilation step.

A simplified CPython execution model is:

Python Source Code
        ↓
Compiler
        ↓
Python Bytecode
        ↓
Python Runtime / Virtual Machine
        ↓
Execution

Bytecode

Bytecode is an intermediate representation of a Python program.

It is important to remember:

Python Bytecode ≠ CPU Machine Code

For example, CPython may cache compiled bytecode in:

__pycache__/

with files such as:

module.cpython-3xx.pyc

Python vs Java

Python

.py
 ↓
Python implementation
 ↓
Python bytecode
 ↓
Python runtime / VM
 ↓
Execution

Java

Java source code is compiled by javac:

javac Hello.java

The process is:

.java
  ↓
javac compiler
  ↓
Java bytecode (.class)
  ↓
JVM
  ↓
Interpretation / JIT compilation
  ↓
Execution

Java therefore uses both compilation and runtime execution techniques.

Interview Answer: Is Python compiled or interpreted?

Python source code is compiled into bytecode by the Python
implementation, and that bytecode is executed by the Python
runtime/virtual machine. Python is commonly classified as an
interpreted language, but saying that Python is only interpreted is
technically incomplete.

Interview Answer: Is Java compiled or interpreted?

Java source code is compiled by javac into platform-independent
bytecode. The JVM executes that bytecode using interpretation and JIT
compilation as appropriate.

5. IDE vs Code Editor

Code Editor

A code editor is primarily used for writing and editing source code.

Examples:

Notepad

Sublime Text

Vim

Visual Studio Code

A code editor typically provides features such as:

Writing code

Editing code

Syntax highlighting

Code completion

Extensions

IDE

IDE = Integrated Development Environment

An IDE combines multiple development tools into one application.

Typical IDE features:

IDE
├── Code Editor
├── Run / Build Tools
├── Debugger
├── Terminal
├── Project / File Management
├── Code Completion
└── Extensions / Plugins

Examples:

PyCharm

Eclipse

IntelliJ IDEA

Visual Studio

Comparison

Feature               Code Editor         IDE

Write code            Yes                 Yes
Syntax highlighting   Yes                 Yes
Code completion       Usually             Yes
Run code              Sometimes           Yes
Debugger              Sometimes           Yes
Project management    Basic--moderate     Usually integrated
Build tools           Usually external    Usually integrated
Extensions            Often               Often
Complexity            Generally simpler   Generally more comprehensive

Important

The distinction is not completely rigid.

VS Code is officially a source-code editor, but extensions can
provide many IDE-like capabilities.

For Python and AI/ML learning, VS Code is a practical choice.

6. Running Python Files

A .py file is a Python source-code file.

Create:

hello.py

Add:

print("Hello Python")

Run from Command Prompt

Suppose the file is located at:

C:\Users\YourName\Documents\Python\hello.py

Move to the folder:

cd C:\Users\YourName\Documents\Python

Run:

python hello.py

Output:

Hello Python

Conceptually:

hello.py
   ↓
python hello.py
   ↓
Python Runtime
   ↓
Output

Run from VS Code

Open hello.py in VS Code.

You can:

Click the Run ▶ button, or

Open the VS Code terminal and run:

python hello.py

Why Use the Terminal?

Running Python from the terminal helps you understand:

Program output

Errors

Exceptions

Python versions

Command-line arguments

python vs python3

Depending on the operating system, you may use:

python hello.py

or:

python3 hello.py

On Windows, python is commonly used after installation.

Check the version:

python --version

Command-Line Arguments

Example:

# hello.py

import sys

print("Hello", sys.argv[1])

Run:

python hello.py Arun

Output:

Hello Arun

Here:

python hello.py Arun
              ↑
           argument

7. Comments

A comment is text written in Python code that is ignored by the
Python interpreter.

Comments are used to:

Explain code

Leave notes

Temporarily disable code

Single-Line Comment

Use #:

# This is a comment
print("Hello Python")

You can also write an inline comment:

x = 10  # Store 10 in x
print(x)

Multiple-Line Comments

Python does not have a dedicated multi-line comment syntax.

Use # on each line:

# This program calculates
# the average of two numbers

a = 10
b = 20

average = (a + b) / 2
print(average)

This is the preferred approach for actual comments.

8. Docstrings

Triple-quoted text is sometimes confused with comments.

"""
This looks like
a multi-line comment.
"""

Technically, this is a multi-line string literal, not a comment.

What is a Docstring?

A docstring is a string literal used to document a module, class,
function, or method.

Example:

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

You can access the docstring at runtime:

print(add.__doc__)

Output:

Return the sum of two numbers.

Important Difference

# comment

A comment is ignored by Python and is mainly intended for developers.

"""docstring"""

A docstring documents Python code and can be accessed at runtime.

Remember

#           → Comment
"""..."""   → Multi-line string / commonly used as a docstring

Do not say:

"A docstring is simply used to write a multi-line string."

A better statement is:

Triple-quoted strings can represent multi-line strings, while a
docstring is a string used specifically for documentation.

9. Indentation

Indentation means the spaces at the beginning of a line of code.

Python uses indentation to define blocks of code.

Unlike C, C++, and Java, Python does not use {} braces to define code
blocks.

Example

if 10 > 5:
    print("10 is greater than 5")

The indentation tells Python that print() belongs to the if block.

Incorrect Indentation

if 10 > 5:
print("10 is greater")

This produces an IndentationError.

Standard Indentation

The standard convention is 4 spaces:

if age >= 18:
    print("Adult")
    print("Can vote")

if and else

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")

Nested Indentation

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")

Each nesting level is normally indented by another 4 spaces.

Indentation in Functions

def greet():
    print("Hello")
    print("Welcome")

greet()

The two print() statements belong to the function because they are
indented.

Interview Question

Why does Python use indentation?

Python uses indentation to define blocks of code and improve code
readability.

Remember

After a statement ending with :, the following block is normally
indented:

if condition:
    # block

for item in items:
    # block

def function():
    # block

class Student:
    # block

Use 4 spaces per indentation level and avoid mixing tabs and spaces.

10. Variables

A variable is a name that refers to an object/value.

Think of a variable as a label attached to an object.

name = "Arun"
age = 22
salary = 30000

Conceptually:

name   → "Arun"
age    → 22
salary → 30000

Creating Variables

Python does not require a separate variable-type declaration:

name = "Arun"
age = 22
height = 5.8
is_student = True

Python determines the type of the object:

print(type(name))        # str
print(type(age))         # int
print(type(height))      # float
print(type(is_student))  # bool

Dynamic Typing

Python is dynamically typed.

x = 10

Later:

x = "Hello"

This is allowed.

The name x can refer to objects of different types at different times.

x → 10
 ↓
x → "Hello"

Variable Naming Rules

Valid

name = "Arun"
age2 = 22
student_name = "Arun"
_total = 100

Invalid

2age = 22
student-name = "Arun"
class = "Python"

Rules

A variable name cannot start with a number.

A variable name cannot contain -.

Do not use Python keywords as variable names.

Multiple Assignment

name, age, city = "Arun", 22, "Madurai"

Equivalent to:

name = "Arun"
age = 22
city = "Madurai"

You can also assign the same value:

a = b = c = 10

Changing a Variable

age = 20
print(age)

age = 21
print(age)

Output:

20
21

The name now refers to a different object.

Variables and Objects

Python variables are better understood as names/references bound to
objects.

x = 10
y = x

Conceptually:

x ──┐
    ↓
  ┌─────┐
  │ 10  │
  │ int │
  └─────┘
    ↑
y ──┘

Both x and y refer to the same integer object in this example.

This model becomes important when learning:

Mutable vs immutable objects

Lists

Dictionaries

Function arguments

Object identity

Interview Question

Does Python have variables?

A technically accurate answer is:

Yes. Python variables are names/references bound to objects rather
than fixed memory boxes with permanently assigned types.

11. Naming Conventions

Naming conventions are standard ways of naming variables, functions,
classes, constants, and other Python objects.

Variables → snake_case

student_name = "Arun"
student_age = 22
total_marks = 450

Functions → snake_case

def calculate_salary():
    pass

def get_student_details():
    pass

Classes → PascalCase

Each word starts with a capital letter:

class Student:
    pass

class BankAccount:
    pass

Comparison:

student_details → variable/function
StudentDetails  → class

Constants → UPPER_CASE

PI = 3.14159
MAX_SIZE = 100
DATABASE_URL = "localhost"

Python does not technically enforce constants as immutable. Uppercase
naming is a convention that tells developers the value is intended to
remain unchanged.

Internal/Private Convention → _name

A single leading underscore commonly indicates internal use:

_internal_value = 10

Example:

class Student:
    def __init__(self):
        self._age = 22

This is a convention, not strict access control.

Special / Magic Methods → __name__

Python special methods often use double underscores:

class Student:
    def __init__(self):
        pass

Examples:

__init__
__str__
__len__
__add__

These are commonly called dunder methods ("double underscore").

Quick Reference

Purpose                       Convention     Example

Variable                      snake_case   student_name
Function                      snake_case   calculate_salary()
Class                         PascalCase   StudentDetails
Constant                      UPPER_CASE   MAX_SIZE
Internal/private convention   _name        _age
Special method                __name__     __init__()

12. Input and Output

Input means taking data from the user or program environment.

Output means displaying or producing data for the user or another
destination.

The two basic Python functions are:

input()
print()

Output --- print()

print() displays output.

print("Hello Python")

Output:

Hello Python

Numbers can also be printed:

print(10)
print(10 + 20)

Output:

10
30

Multiple values:

name = "Arun"
age = 22

print(name, age)

Output:

Arun 22

Input --- input()

input() takes input from the user.

name = input("Enter your name: ")

print("Hello", name)

If the user enters:

Arun

Output:

Enter your name: Arun
Hello Arun

Important

input() returns a string (str) by default.

Taking Integer Input

age = input("Enter your age: ")

print(type(age))

If the user enters 22, the type is still:

<class 'str'>

To convert it to an integer:

age = int(input("Enter your age: "))

print(type(age))

Output:

<class 'int'>

Example: Adding Two Numbers

Incorrect

a = input("Enter first number: ")
b = input("Enter second number: ")

print(a + b)

If the user enters:

10
20

Output:

1020

Why?

Because:

"10" + "20"
↓
"1020"

Both values are strings.

Correct

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)

Output:

Enter first number: 10
Enter second number: 20
30

13. Input → Processing → Output

This is a fundamental programming pattern:

INPUT
  ↓
PROCESSING
  ↓
OUTPUT

Example:

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area =", area)

For:

length = 10
width = 5

Output:

Area = 50.0

14. print() Formatting with f-Strings

f-strings provide a clean way to include variables inside strings.

name = "Arun"
age = 22

print(f"My name is {name} and I am {age} years old.")

Output:

My name is Arun and I am 22 years old.

This is generally cleaner than:

print("My name is", name, "and I am", age, "years old.")

15. Interview Quick Revision

Python Interpreter

A Python interpreter/runtime is software that executes Python
programs.

REPL

REPL stands for Read, Evaluate, Print, Loop.

Bytecode

Bytecode is an intermediate representation executed by the Python
runtime/virtual machine. It is not CPU machine code.

Python: Compiled or Interpreted?

Python has a compilation step that produces bytecode, which is then
executed by the Python runtime. Python is commonly classified as an
interpreted language.

Java: Compiled or Interpreted?

Java source code is compiled by javac into bytecode. The JVM
executes that bytecode using interpretation and JIT compilation as
appropriate.

IDE

IDE stands for Integrated Development Environment and combines code
editing, running, debugging, project management, and other development
tools.

Comment

A comment is text ignored by Python and is mainly used to explain code
or leave notes.

Docstring

A docstring is a string literal used to document a module, class,
function, or method.

Indentation

Python uses indentation to define blocks of code.

Variable

A Python variable is a name/reference bound to an object.

Dynamic Typing

Python is dynamically typed, meaning a name can refer to objects of
different types at different times.

input()

input() reads user input and returns it as a string by default.

print()

print() displays output to the standard output stream.

Summary

The concepts covered so far:

Python Installation
        ↓
Python Interpreter
        ↓
Compiler & Bytecode
        ↓
IDE vs Code Editor
        ↓
Running .py Files
        ↓
Comments & Docstrings
        ↓
Indentation
        ↓
Variables
        ↓
Naming Conventions
        ↓
Input & Output
