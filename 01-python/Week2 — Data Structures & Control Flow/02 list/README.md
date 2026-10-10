# 6. Tuples in Python

---

## 1. Introduction to Tuples

A **tuple** is a built-in Python data type used to store multiple items in a single variable.

**Key Characteristics:**

- **Ordered:** Maintains the order of elements.
- **Immutable:** Elements cannot be reassigned after creation.
- **Duplicates allowed:** The same value can appear multiple times.
- **Multiple data types:** Can store different data types.
- **Indexing and slicing:** Supports accessing individual elements and ranges.

**Example:**

```python
numbers = (10, 20, 30, 40)

print(numbers)
print(type(numbers))
```

**Output:**

```text
(10, 20, 30, 40)
<class 'tuple'>
```

---

## 2. Tuple Creation

Tuples are commonly created using parentheses `()` and comma-separated values.

### Example 1: Tuple of Integers

```python
numbers = (10, 20, 30, 40, 50)

print(numbers)
```

**Output:**

```text
(10, 20, 30, 40, 50)
```

### Example 2: Tuple of Strings

```python
names = ("Arun", "Priya", "Kumar")

print(names)
```

**Output:**

```text
('Arun', 'Priya', 'Kumar')
```

### Example 3: Tuple with Different Data Types

```python
data = (10, "Python", 3.14, True)

print(data)
```

**Output:**

```text
(10, 'Python', 3.14, True)
```

### Example 4: Single-Element Tuple

A single-element tuple must contain a trailing comma.

```python
a = (10,)
b = (10)

print(type(a))
print(type(b))
```

**Output:**

```text
<class 'tuple'>
<class 'int'>
```

**Note:** `(10,)` is a tuple, whereas `(10)` is an integer.

---

## 3. Tuple Indexing

**Indexing** is used to access individual elements from a tuple.

- **Positive indexing:** Starts from `0`.
- **Negative indexing:** Starts from `-1` at the end.

### Example 1: Positive Indexing

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[0])
print(numbers[2])
print(numbers[4])
```

**Output:**

```text
10
30
50
```

### Example 2: Negative Indexing

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[-1])
print(numbers[-2])
print(numbers[-5])
```

**Output:**

```text
50
40
10
```

**Index Reference:**

| Positive Index | Negative Index | Value |
|---:|---:|---:|
| `0` | `-5` | `10` |
| `1` | `-4` | `20` |
| `2` | `-3` | `30` |
| `3` | `-2` | `40` |
| `4` | `-1` | `50` |

**Note:** Accessing an invalid index raises an `IndexError`.

---

## 4. Tuple Slicing

**Slicing** is used to access a range of elements from a tuple.

**Syntax:**

```python
tuple[start:stop:step]
```

- `start`: Starting index (included).
- `stop`: Ending index (excluded).
- `step`: Number of positions to skip.

### Example 1: Basic Slicing

```python
numbers = (10, 20, 30, 40, 50, 60)

print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
```

**Output:**

```text
(20, 30, 40)
(10, 20, 30)
(40, 50, 60)
```

### Example 2: Slicing with Step

```python
numbers = (10, 20, 30, 40, 50, 60)

print(numbers[::2])
print(numbers[1::2])
```

**Output:**

```text
(10, 30, 50)
(20, 40, 60)
```

### Example 3: Reversing a Tuple

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[::-1])
```

**Output:**

```text
(50, 40, 30, 20, 10)
```

**Note:** Slicing returns a new tuple and does not modify the original tuple.

---

## 5. Tuple Unpacking

**Tuple unpacking** is the process of assigning tuple elements to multiple variables in a single statement.

### Example 1: Basic Unpacking

```python
student = ("Arun", 22, "Python")

name, age, course = student

print(name)
print(age)
print(course)
```

**Output:**

```text
Arun
22
Python
```

### Example 2: Unpacking Numbers

```python
numbers = (10, 20, 30)

a, b, c = numbers

print(a)
print(b)
print(c)
```

**Output:**

```text
10
20
30
```

### Example 3: Swapping Variables

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

**Output:**

```text
20
10
```

### Example 4: Unpacking with the `*` Operator

The `*` operator collects the remaining elements into a list.

```python
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

**Output:**

```text
10
[20, 30, 40]
50
```

**Note:** Without starred unpacking, the number of variables must match the number of elements.

---

## 6. Tuple vs List

Both tuples and lists store multiple items, but their main difference is **mutability**.

| Feature | Tuple | List |
|---|---|---|
| Syntax | `(10, 20, 30)` | `[10, 20, 30]` |
| Ordered | Yes | Yes |
| Mutable | No | Yes |
| Indexing | Supported | Supported |
| Slicing | Supported | Supported |
| Duplicates | Allowed | Allowed |
| Different data types | Allowed | Allowed |
| Adding or removing items | Not directly supported | Supported |

### Example 1: List Is Mutable

```python
numbers = [10, 20, 30]

numbers[0] = 100
numbers.append(40)

print(numbers)
```

**Output:**

```text
[100, 20, 30, 40]
```

### Example 2: Tuple Is Immutable

```python
numbers = (10, 20, 30)

numbers[0] = 100

print(numbers)
```

**Output:**

```text
TypeError: 'tuple' object does not support item assignment
```

**Explanation:** Tuple elements cannot be reassigned after creation.

### When to Use Tuples

- When storing fixed collections of values.
- When representing coordinates or RGB color values.
- When individual elements should not be reassigned.

### When to Use Lists

- When elements need to be modified.
- When items need to be added or removed.
- When working with collections that change frequently.

---

## 7. Useful Tuple Operations

### Example 1: `len()` — Find the Number of Elements

```python
numbers = (10, 20, 30, 40)

print(len(numbers))
```

**Output:**

```text
4
```

### Example 2: `count()` — Count Occurrences

```python
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
```

**Output:**

```text
3
```

### Example 3: `index()` — Find the First Matching Index

```python
numbers = (10, 20, 30, 40)

print(numbers.index(30))
```

**Output:**

```text
2
```

### Example 4: Membership Operators

```python
numbers = (10, 20, 30, 40)

print(20 in numbers)
print(50 not in numbers)
```

**Output:**

```text
True
True
```

### Example 5: Tuple Concatenation

The `+` operator combines two tuples into a new tuple.

```python
a = (10, 20)
b = (30, 40)

result = a + b

print(result)
```

**Output:**

```text
(10, 20, 30, 40)
```

### Example 6: Tuple Repetition

The `*` operator repeats tuple elements.

```python
numbers = (10, 20)

print(numbers * 3)
```

**Output:**

```text
(10, 20, 10, 20, 10, 20)
```

---

## 8. Practice Tasks

### Level 1: Tuple Creation

1. Create a tuple containing five integers and print it.
2. Create a tuple containing your name, age, and course.
3. Create a single-element tuple containing `100` and print its type.

### Level 2: Tuple Indexing

4. Create a tuple containing six numbers. Print the first, third, and last elements.
5. Print the second-last element using negative indexing.
6. Access and print an element using its index.

### Level 3: Tuple Slicing

7. Create a tuple containing eight numbers. Print the first four elements.
8. Print the last three elements.
9. Print every second element.
10. Reverse the tuple using slicing.

### Level 4: Tuple Unpacking

11. Unpack a tuple containing three student details into three variables.
12. Unpack `(10, 20, 30)` into three variables and print their sum.
13. Swap two variables using tuple unpacking.
14. Use the `*` operator to collect the middle elements of a tuple.

### Level 5: Tuple vs List

15. Create a list and a tuple containing the same three numbers.
16. Modify the first element of the list.
17. Try modifying the first element of the tuple and observe the error.
18. Count how many times `20` appears in `(10, 20, 30, 20, 40, 20)`.
19. Find the index of `30` in a tuple.
20. Check whether `40` exists in a tuple using the `in` operator.

---

## 9. Quick Revision

| Concept | Description |
|---|---|
| Tuple | Ordered, immutable collection |
| Creation | Parentheses `()` and comma-separated values |
| Indexing | Access individual elements |
| Slicing | Access a range of elements |
| Unpacking | Assign elements to multiple variables |
| `len()` | Returns the number of elements |
| `count()` | Counts occurrences of a value |
| `index()` | Returns the first matching index |
| `+` | Concatenates tuples |
| `*` | Repeats tuple elements |

---

### Key Takeaway

**Tuples are ordered and immutable, while lists are ordered and mutable.**

Use tuples for fixed collections and lists when the collection needs modification.
