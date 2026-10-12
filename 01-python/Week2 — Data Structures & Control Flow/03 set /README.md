# 7. Sets in Python

---

## 1. What is a Set?

A **set** is a built-in Python data type used to store multiple **unique elements** in a single variable.

### Key Features

- **Unordered:** Elements do not have a fixed position.
- **Unique elements:** Duplicate values are automatically removed.
- **Mutable:** We can add or remove elements.
- **Unindexed:** Sets do not support indexing or slicing.
- **Multiple data types:** A set can contain different hashable data types.

### Example

```python
numbers = {10, 20, 30, 40}

print(numbers)
```

**Output:**

```text
{10, 20, 30, 40}
```

> Note: Sets are unordered, so the output order is not guaranteed.

---

## 2. Creating Sets

We can create a set using curly braces `{}` or the `set()` constructor.

### Example 1: Using Curly Braces

```python
fruits = {"apple", "banana", "orange"}

print(fruits)
print(type(fruits))
```

**Output:**

```text
{'apple', 'banana', 'orange'}
<class 'set'>
```

### Example 2: Creating a Set with Duplicate Values

Duplicate elements are automatically removed.

```python
numbers = {10, 20, 10, 30, 20}

print(numbers)
```

**Output:**

```text
{10, 20, 30}
```

### Example 3: Creating an Empty Set

Use `set()` to create an empty set.

```python
empty_set = set()

print(empty_set)
print(type(empty_set))
```

**Output:**

```text
set()
<class 'set'>
```

**Important:** `{}` creates an empty dictionary, not an empty set.

```python
a = {}

print(type(a))  # <class 'dict'>
```

---

## 3. Adding Elements to a Set

Python provides two main methods for adding elements to a set.

### `add()`

Adds a single element to the set.

```python
fruits = {"apple", "banana"}

fruits.add("orange")

print(fruits)
```

**Output:**

```text
{'apple', 'banana', 'orange'}
```

Adding an element that already exists does not create a duplicate.

```python
numbers = {10, 20, 30}

numbers.add(20)

print(numbers)
```

**Output:**

```text
{10, 20, 30}
```

### `update()`

Adds multiple elements from an iterable, such as a list, tuple, or another set.

```python
numbers = {10, 20}

numbers.update([30, 40, 50])

print(numbers)
```

**Output:**

```text
{10, 20, 30, 40, 50}
```

**Difference:**

- `add()` → Adds one element.
- `update()` → Adds multiple elements.

---

## 4. Removing Elements from a Set

Python provides several methods to remove elements.

### `remove()`

Removes the specified element. Raises a `KeyError` if the element does not exist.

```python
numbers = {10, 20, 30, 40}

numbers.remove(20)

print(numbers)
```

**Output:**

```text
{10, 30, 40}
```

### `discard()`

Removes the specified element without raising an error if it does not exist.

```python
numbers = {10, 20, 30}

numbers.discard(50)

print(numbers)
```

**Output:**

```text
{10, 20, 30}
```

### `pop()`

Removes and returns an arbitrary element from the set. Because sets are unordered, you should not expect a particular element to be removed.

```python
numbers = {10, 20, 30}

removed = numbers.pop()

print("Removed:", removed)
print("Remaining:", numbers)
```

**Note:** The removed element may vary.

### `clear()`

Removes all elements from the set.

```python
numbers = {10, 20, 30}

numbers.clear()

print(numbers)
```

**Output:**

```text
set()
```

### Quick Comparison

| Method | Purpose | If element is absent |
|---|---|---|
| `add()` | Adds one element | Adds it |
| `update()` | Adds multiple elements | Adds available elements |
| `remove()` | Removes an element | Raises `KeyError` |
| `discard()` | Removes an element | No error |
| `pop()` | Removes an arbitrary element | Raises `KeyError` if empty |
| `clear()` | Removes all elements | No error |

---

## 5. Union of Sets

The **union** operation returns all unique elements from two or more sets.

### Symbol: `|`

### Method: `union()`

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A | B

print(result)
```

**Output:**

```text
{1, 2, 3, 4, 5, 6}
```

### Using the `union()` Method

```python
A = {1, 2, 3}
B = {3, 4, 5}

result = A.union(B)

print(result)
```

**Output:**

```text
{1, 2, 3, 4, 5}
```

**Remember:** Union combines elements from both sets and removes duplicates.

---

## 6. Intersection of Sets

The **intersection** operation returns only the elements common to both sets.

### Symbol: `&`

### Method: `intersection()`

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A & B

print(result)
```

**Output:**

```text
{3, 4}
```

### Using the `intersection()` Method

```python
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

result = A.intersection(B)

print(result)
```

**Output:**

```text
{40, 30}
```

**Remember:** Intersection returns only common elements.

---

## 7. Difference of Sets

The **difference** operation returns elements that exist in the first set but not in the second set.

### Symbol: `-`

### Method: `difference()`

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A - B)
print(B - A)
```

**Output:**

```text
{1, 2}
{5, 6}
```

### Using the `difference()` Method

```python
A = {10, 20, 30, 40}
B = {30, 40, 50}

result = A.difference(B)

print(result)
```

**Output:**

```text
{10, 20}
```

**Remember:** Difference is directional. `A - B` is not necessarily the same as `B - A`.

---

## 8. Symmetric Difference of Sets

The **symmetric difference** operation returns elements that exist in either set, but not in both.

### Symbol: `^`

### Method: `symmetric_difference()`

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A ^ B

print(result)
```

**Output:**

```text
{1, 2, 5, 6}
```

### Using the `symmetric_difference()` Method

```python
A = {10, 20, 30}
B = {30, 40, 50}

result = A.symmetric_difference(B)

print(result)
```

**Output:**

```text
{10, 20, 40, 50}
```

**Remember:** Symmetric difference excludes common elements and keeps elements unique to either set.

---

## 9. Set Operations Summary

Consider the following sets:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

| Operation | Symbol | Result |
|---|---|---|
| Union | `A \| B` | `{1, 2, 3, 4, 5, 6}` |
| Intersection | `A & B` | `{3, 4}` |
| Difference | `A - B` | `{1, 2}` |
| Reverse difference | `B - A` | `{5, 6}` |
| Symmetric difference | `A ^ B` | `{1, 2, 5, 6}` |

---

## 10. Checking Membership in a Set

Use the `in` and `not in` operators to check whether an element exists in a set.

### Using `in`

```python
fruits = {"apple", "banana", "orange"}

print("apple" in fruits)
print("grapes" in fruits)
```

**Output:**

```text
True
False
```

### Using `not in`

```python
fruits = {"apple", "banana", "orange"}

print("grapes" not in fruits)
```

**Output:**

```text
True
```

---

## 11. Important Set Rules

1. Sets do not allow duplicate elements.
2. Sets do not support indexing or slicing.
3. Sets are mutable, so elements can be added or removed.
4. Set elements must be hashable. For example, numbers, strings, and tuples containing only hashable elements can be stored in sets.
5. Lists and dictionaries cannot be elements of a set.
6. An empty set must be created using `set()`.
7. Set operations return a set of unique elements.
8. Use `remove()` when a missing element should raise an error; use `discard()` when it should not.

### Example: Indexing Is Not Supported

```python
numbers = {10, 20, 30}

# print(numbers[0])  # TypeError
```

Sets do not have positional indexes.

---

## 12. Practical Example

Suppose two students attend different courses. We want to find which courses they share and which courses only one student attends.

```python
student_1 = {"Python", "SQL", "HTML"}
student_2 = {"Python", "Java", "CSS"}

print("All courses:", student_1 | student_2)
print("Common courses:", student_1 & student_2)
print("Only Student 1:", student_1 - student_2)
print("Only one student:", student_1 ^ student_2)
```

**Output:**

```text
All courses: {'Python', 'SQL', 'HTML', 'Java', 'CSS'}
Common courses: {'Python'}
Only Student 1: {'SQL', 'HTML'}
Only one student: {'SQL', 'HTML', 'Java', 'CSS'}
```

> Set output order may vary.

---

## 13. Quick Revision

- **Set:** Stores unique elements.
- **Create:** `{1, 2, 3}` or `set()`.
- **Add one element:** `add()`.
- **Add multiple elements:** `update()`.
- **Remove with an error if absent:** `remove()`.
- **Remove without an error if absent:** `discard()`.
- **Union:** `|` — all unique elements.
- **Intersection:** `&` — common elements.
- **Difference:** `-` — elements in the first set only.
- **Symmetric difference:** `^` — elements in either set, but not both.
- **Membership:** `in`, `not in`.

---

**Next topic:** Set methods and set comparisons, including `issubset()`, `issuperset()`, and `isdisjoint()`.
