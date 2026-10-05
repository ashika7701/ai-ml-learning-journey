# 🐍 Python Operators

**Operators** are special symbols or keywords used to perform operations on values and variables.

### Example

```python
a = 10
b = 5

print(a + b)
```

**Output:**

```text
15
```

Here:

* `+` → Operator
* `a` and `b` → Operands
* `a + b` → Expression

---

# 📚 Types of Operators in Python

Python provides several types of operators:

1. **Arithmetic Operators**
2. **Comparison Operators**
3. **Logical Operators**
4. **Assignment Operators**
5. **Membership Operators**
6. **Identity Operators**

---

# 1. 🧮 Arithmetic Operators

Arithmetic operators are used to perform **mathematical operations**.

| Operator | Name           | Example   |     Result |
| -------- | -------------- | --------- | ---------: |
| `+`      | Addition       | `10 + 3`  |       `13` |
| `-`      | Subtraction    | `10 - 3`  |        `7` |
| `*`      | Multiplication | `10 * 3`  |       `30` |
| `/`      | Division       | `10 / 3`  | `3.333...` |
| `%`      | Modulus        | `10 % 3`  |        `1` |
| `**`     | Exponentiation | `10 ** 3` |     `1000` |
| `//`     | Floor Division | `10 // 3` |        `3` |

---

## 1.1 `+` Addition

Adds two values.

```python
a = 10
b = 5

print(a + b)
```

**Output:**

```text
15
```

---

## 1.2 `-` Subtraction

Subtracts the second value from the first value.

```python
a = 10
b = 5

print(a - b)
```

**Output:**

```text
5
```

---

## 1.3 `*` Multiplication

Multiplies two values.

```python
a = 10
b = 5

print(a * b)
```

**Output:**

```text
50
```

---

## 1.4 `/` Division

Divides one value by another.

The `/` operator **always returns a float**.

```python
a = 10
b = 2

print(a / b)
```

**Output:**

```text
5.0
```

Another example:

```python
print(10 / 3)
```

**Output:**

```text
3.3333333333333335
```

---

## 1.5 `%` Modulus

Returns the **remainder** after division.

```python
a = 10
b = 3

print(a % b)
```

**Output:**

```text
1
```

### Practical Example

The modulus operator is commonly used to check whether a number is even or odd.

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Output:**

```text
Even
```

---

## 1.6 `**` Exponentiation

Raises a number to a specified power.

```python
a = 2
b = 3

print(a ** b)
```

**Output:**

```text
8
```

This means:

```text
2³ = 2 × 2 × 2 = 8
```

---

## 1.7 `//` Floor Division

Performs division and returns the **floor value** of the result.

```python
a = 10
b = 3

print(a // b)
```

**Output:**

```text
3
```

Compare:

```python
print(10 / 3)
print(10 // 3)
```

**Output:**

```text
3.3333333333333335
3
```

> ⚠️ With negative numbers, floor division rounds **toward negative infinity**, not simply toward zero.

```python
print(-10 // 3)
```

**Output:**

```text
-4
```

---

# 2. ⚖️ Comparison Operators

Comparison operators are used to **compare two values**.

They return either:

```text
True
```

or

```text
False
```

| Operator | Meaning                  | Example    |
| -------- | ------------------------ | ---------- |
| `==`     | Equal to                 | `10 == 10` |
| `!=`     | Not equal to             | `10 != 5`  |
| `>`      | Greater than             | `10 > 5`   |
| `<`      | Less than                | `5 < 10`   |
| `>=`     | Greater than or equal to | `10 >= 10` |
| `<=`     | Less than or equal to    | `5 <= 10`  |

---

## 2.1 `==` Equal To

Checks whether two values are equal.

```python
a = 10
b = 10

print(a == b)
```

**Output:**

```text
True
```

> 💡 `==` is used for **comparison**, while `=` is used for **assignment**.

---

## 2.2 `!=` Not Equal To

Checks whether two values are different.

```python
a = 10
b = 5

print(a != b)
```

**Output:**

```text
True
```

---

## 2.3 `>` Greater Than

Checks whether the left value is greater than the right value.

```python
a = 10
b = 5

print(a > b)
```

**Output:**

```text
True
```

---

## 2.4 `<` Less Than

Checks whether the left value is less than the right value.

```python
a = 5
b = 10

print(a < b)
```

**Output:**

```text
True
```

---

## 2.5 `>=` Greater Than or Equal To

Checks whether the left value is greater than or equal to the right value.

```python
a = 10

print(a >= 10)
```

**Output:**

```text
True
```

---

## 2.6 `<=` Less Than or Equal To

Checks whether the left value is less than or equal to the right value.

```python
a = 10

print(a <= 10)
```

**Output:**

```text
True
```

---

# 3. 🧠 Logical Operators

Logical operators are used to **combine or modify conditions**.

Python has three logical operators:

| Operator | Meaning                                |
| -------- | -------------------------------------- |
| `and`    | True if both conditions are true       |
| `or`     | True if at least one condition is true |
| `not`    | Reverses the Boolean result            |

---

## 3.1 `and`

Returns `True` when **both conditions are true**.

```python
age = 25

print(age >= 18 and age <= 60)
```

**Output:**

```text
True
```

### Truth Table

| A     | B     | `A and B` |
| ----- | ----- | --------- |
| True  | True  | True      |
| True  | False | False     |
| False | True  | False     |
| False | False | False     |

### Practical Example

```python
age = 25
has_id = True

if age >= 18 and has_id:
    print("Allowed")
```

**Output:**

```text
Allowed
```

---

## 3.2 `or`

Returns `True` when **at least one condition is true**.

```python
age = 16

print(age < 18 or age > 60)
```

**Output:**

```text
True
```

### Truth Table

| A     | B     | `A or B` |
| ----- | ----- | -------- |
| True  | True  | True     |
| True  | False | True     |
| False | True  | True     |
| False | False | False    |

---

## 3.3 `not`

Reverses the Boolean value.

```python
value = True

print(not value)
```

**Output:**

```text
False
```

Another example:

```python
value = False

print(not value)
```

**Output:**

```text
True
```

### Truth Table

| A     | `not A` |
| ----- | ------- |
| True  | False   |
| False | True    |

---

# 4. 📝 Assignment Operators

Assignment operators are used to **assign values to variables**.

| Operator | Example  | Equivalent To |
| -------- | -------- | ------------- |
| `=`      | `x = 10` | `x = 10`      |
| `+=`     | `x += 5` | `x = x + 5`   |
| `-=`     | `x -= 5` | `x = x - 5`   |
| `*=`     | `x *= 5` | `x = x * 5`   |
| `/=`     | `x /= 5` | `x = x / 5`   |

---

## 4.1 `=` Assignment

Assigns a value to a variable.

```python
x = 10

print(x)
```

**Output:**

```text
10
```

---

## 4.2 `+=`

Adds a value to the variable and assigns the result back.

```python
x = 10

x += 5

print(x)
```

**Output:**

```text
15
```

Equivalent to:

```python
x = x + 5
```

---

## 4.3 `-=`

Subtracts a value and assigns the result back.

```python
x = 10

x -= 3

print(x)
```

**Output:**

```text
7
```

Equivalent to:

```python
x = x - 3
```

---

## 4.4 `*=`

Multiplies a variable and assigns the result back.

```python
x = 10

x *= 3

print(x)
```

**Output:**

```text
30
```

Equivalent to:

```python
x = x * 3
```

---

## 4.5 `/=`

Divides a variable and assigns the result back.

```python
x = 10

x /= 2

print(x)
```

**Output:**

```text
5.0
```

Equivalent to:

```python
x = x / 2
```

> 💡 `/=` may change an integer value into a `float`.

---

# 5. 🔎 Membership Operators

Membership operators are used to **check whether a value exists inside a sequence or collection**.

Python provides:

* `in`
* `not in`

They return `True` or `False`.

---

## 5.1 `in`

Checks whether a value **exists** in a sequence.

### Example with String

```python
text = "Python"

print("P" in text)
```

**Output:**

```text
True
```

Another example:

```python
print("Java" in "Python")
```

**Output:**

```text
False
```

### Example with List

```python
languages = ["Python", "Java", "C++"]

print("Python" in languages)
```

**Output:**

```text
True
```

---

## 5.2 `not in`

Checks whether a value **does not exist** in a sequence.

```python
languages = ["Python", "Java", "C++"]

print("JavaScript" not in languages)
```

**Output:**

```text
True
```

### Example

```python
text = "Python"

print("Java" not in text)
```

**Output:**

```text
True
```

---

# 6. 🆔 Identity Operators

Identity operators are used to check whether **two variables refer to the same object in memory**.

Python provides:

* `is`
* `is not`

| Operator | Meaning                                                  |
| -------- | -------------------------------------------------------- |
| `is`     | Checks whether two references point to the same object   |
| `is not` | Checks whether two references point to different objects |

> ⚠️ **Important:** `is` is different from `==`.

---

## 6.1 `is`

Checks whether two variables refer to the **same object**.

```python
a = None
b = None

print(a is b)
```

**Output:**

```text
True
```

A very common use of `is` is checking for `None`:

```python
value = None

if value is None:
    print("No value")
```

**Output:**

```text
No value
```

---

## 6.2 `is not`

Checks whether two variables do **not** refer to the same object.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is not b)
```

**Output:**

```text
True
```

Although `a` and `b` contain the same values, they are separate list objects.

---

# ⚠️ `==` vs `is`

This is an **important Python concept**.

### `==`

Checks whether two objects have **equal values**.

### `is`

Checks whether two variables refer to the **same object**.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

**Output:**

```text
True
False
```

Explanation:

```text
a == b
→ Values are equal → True

a is b
→ Different list objects → False
```

> ⭐ **Rule:** Use `==` for value comparison and `is` mainly for identity checks such as `value is None`.

---

# 📊 Operators — Quick Reference

| Category       | Operators         | Main Purpose            |
| -------------- | ----------------- | ----------------------- |
| **Arithmetic** | `+ - * / % ** //` | Mathematical operations |
| **Comparison** | `== != > < >= <=` | Compare values          |
| **Logical**    | `and or not`      | Combine conditions      |
| **Assignment** | `= += -= *= /=`   | Assign/update values    |
| **Membership** | `in`, `not in`    | Check membership        |
| **Identity**   | `is`, `is not`    | Check object identity   |

---

# 🧠 Easy Way to Remember

```text
Arithmetic
    ↓
Calculate
+  -  *  /  %  **  //

Comparison
    ↓
Compare
==  !=  >  <  >=  <=

Logical
    ↓
Combine conditions
and  or  not

Assignment
    ↓
Store / Update values
=  +=  -=  *=  /=

Membership
    ↓
Check existence
in  /  not in

Identity
    ↓
Check same object
is  /  is not
```

---

# 🎯 Practical Example Using Multiple Operators

```python
age = 25
has_id = True
name = "Python"

if age >= 18 and has_id:
    print("Eligible")

print("Py" in name)
print(name == "Python")
```

**Output:**

```text
Eligible
True
True
```

Here:

* `>=` → Comparison operator
* `and` → Logical operator
* `in` → Membership operator
* `==` → Comparison operator

---

# ⭐ Key Points

1. **Arithmetic operators** perform mathematical calculations.
2. **Comparison operators** return `True` or `False`.
3. **Logical operators** combine conditions.
4. **Assignment operators** assign or update variable values.
5. **Membership operators** check whether a value exists in a sequence.
6. **Identity operators** check whether two references point to the same object.
7. `=` means **assignment**.
8. `==` means **value equality comparison**.
9. `is` means **object identity comparison**.
10. Use `==` for comparing values and `is` for identity checks such as `None`.
