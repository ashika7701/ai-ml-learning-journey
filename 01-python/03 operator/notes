. Logical Operators

Used to combine multiple conditions.

Operator	Meaning
and	Both conditions must be True
or	At least one condition must be True
not	Reverses the result
and
age = 25
salary = 50000

print(age >= 18 and salary >= 30000)

Output:

True

Both conditions are True.

or
age = 16
has_permission = True

print(age >= 18 or has_permission)

Output:

True

At least one condition is True.

not
is_raining = True

print(not is_raining)

Output:

False

Remember:

and → BOTH
or  → ANY ONE
not → REVERSE
4. Assignment Operators

Used to assign values to variables.

Operator	Meaning	Example	Equivalent to
=	Assign	x = 10	x = 10
+=	Add and assign	x += 5	x = x + 5
-=	Subtract and assign	x -= 5	x = x - 5
*=	Multiply and assign	x *= 5	x = x * 5
/=	Divide and assign	x /= 5	x = x / 5
Example
x = 10

x += 5
print(x)       # 15

x -= 3
print(x)       # 12

x *= 2
print(x)       # 24

x /= 4
print(x)       # 6.0
5. Membership Operators

Used to check whether a value exists inside a sequence such as a list, tuple, string, etc.

Operator	Meaning
in	Checks whether a value exists
not in	Checks whether a value does not exist
in
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)

Output:

True
not in
fruits = ["apple", "banana", "mango"]

print("orange" not in fruits)

Output:

True
String example
name = "Python"

print("P" in name)       # True
print("z" not in name)   # True
6. Identity Operators

Used to check whether two variables refer to the same object in memory.

Operator	Meaning
is	Same object
is not	Different objects
Example
a = None

print(a is None)

Output:

True

A common use of is is checking for None:

result = None

if result is None:
    print("No result")

Output:

No result
is not
x = None

print(x is not None)

Output:

False
⚠️ == vs is

This is important:

==  → checks whether values are equal
is  → checks whether they are the same object

For example:

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True
print(a is b)   # False

The lists have the same values, but they are different objects.

Quick Revision Sheet
Category	Operators	Main Purpose
Arithmetic	+ - * / % ** //	Calculations
Comparison	== != > < >= <=	Compare values
Logical	and or not	Combine conditions
Assignment	= += -= *= /=	Assign/update values
Membership	in, not in	Check existence
Identity	is, is not	Check object identity
Easy way to remember
Arithmetic  → Calculate
Comparison  → Compare
Logical     → Combine conditions
Assignment  → Store / Update
Membership  → Search inside
Identity    → Same object?
AI/ML relevance

You will use these operators constantly in AI/ML Python code:

accuracy = 0.92
threshold = 0.90

if accuracy >= threshold and accuracy <= 1.0:
    print("Good model")
