# 📋 5. Lists in Python

A **list** is a collection used to store multiple values in a single variable.

Lists are created using **square brackets `[]`**.

```python
fruits = ["apple", "banana", "orange"]

print(fruits)
```

### Output

```text
['apple', 'banana', 'orange']
```

---

# 🔹 Characteristics of Lists

Python lists are:

* **Ordered** — elements maintain their position.
* **Mutable** — elements can be changed after creation.
* **Allow duplicates** — the same value can appear multiple times.
* **Heterogeneous** — different data types can be stored.
* **Indexed** — each element has an index.

Example:

```python
data = [10, "Python", 20.5, True]

print(data)
```

---

# 1. Creating Lists

## Empty List

```python
numbers = []

print(numbers)
```

### Output

```text
[]
```

---

## List with Values

```python
numbers = [10, 20, 30, 40]

print(numbers)
```

### Output

```text
[10, 20, 30, 40]
```

---

## List with Duplicate Values

Lists allow duplicate values.

```python
numbers = [10, 20, 10, 30]

print(numbers)
```

### Output

```text
[10, 20, 10, 30]
```

---

## List with Different Data Types

```python
student = ["Ashika", 25, 85.5, True]

print(student)
```

A list can contain:

* `str`
* `int`
* `float`
* `bool`
* other lists

---

## Creating a List Using `list()`

```python
name = "Python"

letters = list(name)

print(letters)
```

### Output

```text
['P', 'y', 't', 'h', 'o', 'n']
```

---

# 2. Indexing

**Indexing** is used to access individual elements from a list.

Python uses **zero-based indexing**.

```text
List:       [10, 20, 30, 40, 50]
Index:       0   1   2   3   4
Negative:   -5  -4  -3  -2  -1
```

## Positive Indexing

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
print(numbers[4])
```

### Output

```text
10
30
50
```

---

## Negative Indexing

Negative indexing starts from the end.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[-1])
print(numbers[-2])
```

### Output

```text
50
40
```

### Remember

```text
First element  → index 0
Second element → index 1
Last element   → index -1
```

---

# 3. Slicing

**Slicing** is used to extract a portion of a list.

### Syntax

```python
list[start:stop]
```

The `stop` index is **not included**.

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

### Output

```text
[20, 30, 40]
```

---

## Slicing with Step

### Syntax

```python
list[start:stop:step]
```

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0:5:2])
```

### Output

```text
[10, 30, 50]
```

---

## Omitting Start

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[:3])
```

### Output

```text
[10, 20, 30]
```

---

## Omitting Stop

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[2:])
```

### Output

```text
[30, 40, 50]
```

---

## Reverse Using Slicing

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[::-1])
```

### Output

```text
[50, 40, 30, 20, 10]
```

---

# 4. Adding Elements

There are three important ways to add elements:

* `append()`
* `extend()`
* `insert()`

---

## `append()`

Adds **one element** to the end of the list.

### Syntax

```python
list.append(value)
```

Example:

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

### Output

```text
[10, 20, 30, 40]
```

### Important

`append()` adds the entire value as **one element**.

```python
numbers = [10, 20]

numbers.append([30, 40])

print(numbers)
```

### Output

```text
[10, 20, [30, 40]]
```

---

## `extend()`

Adds **multiple elements** to the end of the list.

### Syntax

```python
list.extend(iterable)
```

Example:

```python
numbers = [10, 20]

numbers.extend([30, 40])

print(numbers)
```

### Output

```text
[10, 20, 30, 40]
```

### `append()` vs `extend()`

```python
numbers = [10, 20]

numbers.append([30, 40])

print(numbers)
```

Output:

```text
[10, 20, [30, 40]]
```

Whereas:

```python
numbers = [10, 20]

numbers.extend([30, 40])

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

> **`append()` → adds one element**
> **`extend()` → adds multiple elements**

---

## `insert()`

Adds an element at a **specific position**.

### Syntax

```python
list.insert(index, value)
```

Example:

```python
numbers = [10, 20, 40]

numbers.insert(2, 30)

print(numbers)
```

### Output

```text
[10, 20, 30, 40]
```

---

# 5. Removing Elements

The main methods used to remove elements are:

* `remove()`
* `pop()`

---

## `remove()`

Removes the **first occurrence** of a specified value.

### Syntax

```python
list.remove(value)
```

Example:

```python
numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)
```

### Output

```text
[10, 30, 20]
```

Only the **first `20`** is removed.

> `remove()` works using the **value**.

---

## `pop()`

Removes and returns an element using its **index**.

### Syntax

```python
list.pop(index)
```

Example:

```python
numbers = [10, 20, 30, 40]

value = numbers.pop(2)

print(value)
print(numbers)
```

### Output

```text
30
[10, 20, 40]
```

### `pop()` Without Index

If no index is provided, `pop()` removes the **last element**.

```python
numbers = [10, 20, 30]

numbers.pop()

print(numbers)
```

### Output

```text
[10, 20]
```

### `remove()` vs `pop()`

| Method     | Works With | Returns Removed Value |
| ---------- | ---------- | --------------------- |
| `remove()` | Value      | No                    |
| `pop()`    | Index      | Yes                   |

---

# 6. Updating Elements

Lists are **mutable**, so their elements can be changed.

### Syntax

```python
list[index] = new_value
```

Example:

```python
numbers = [10, 20, 30]

numbers[1] = 200

print(numbers)
```

### Output

```text
[10, 200, 30]
```

The value at index `1` changed from `20` to `200`.

---

## Updating Multiple Elements

Slicing can also be used to update multiple elements.

```python
numbers = [10, 20, 30, 40]

numbers[1:3] = [200, 300]

print(numbers)
```

### Output

```text
[10, 200, 300, 40]
```

---

# 7. Nested Lists

A **nested list** is a list that contains another list.

Example:

```python
numbers = [[10, 20], [30, 40], [50, 60]]

print(numbers)
```

### Output

```text
[[10, 20], [30, 40], [50, 60]]
```

---

## Accessing Nested List Elements

```python
numbers = [[10, 20], [30, 40], [50, 60]]

print(numbers[0])
print(numbers[0][1])
```

### Output

```text
[10, 20]
20
```

Explanation:

```text
numbers[0]       → [10, 20]
numbers[0][1]    → 20
```

---

# 8. Sorting Lists

The `sort()` method arranges list elements in order.

### Ascending Order

```python
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)
```

### Output

```text
[10, 20, 30, 40]
```

---

## Descending Order

Use `reverse=True`.

```python
numbers = [40, 10, 30, 20]

numbers.sort(reverse=True)

print(numbers)
```

### Output

```text
[40, 30, 20, 10]
```

---

## Sorting Strings

```python
names = ["Charlie", "Alice", "Bob"]

names.sort()

print(names)
```

### Output

```text
['Alice', 'Bob', 'Charlie']
```

---

# 9. Reversing a List

The `reverse()` method reverses the order of elements.

```python
numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)
```

### Output

```text
[40, 30, 20, 10]
```

### `sort(reverse=True)` vs `reverse()`

```python
numbers.sort(reverse=True)
```

Sorts the values in **descending order**.

```python
numbers.reverse()
```

Simply reverses the **current order**.

---

# 10. Counting Elements

The `count()` method counts how many times a value appears in a list.

### Syntax

```python
list.count(value)
```

Example:

```python
numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))
```

### Output

```text
3
```

The value `10` occurs **3 times**.

---

# 11. Finding the Index of an Element

The `index()` method returns the index of the **first occurrence** of a value.

### Syntax

```python
list.index(value)
```

Example:

```python
numbers = [10, 20, 30, 40]

print(numbers.index(30))
```

### Output

```text
2
```

---

## `index()` with Duplicate Values

```python
numbers = [10, 20, 30, 20, 40]

print(numbers.index(20))
```

### Output

```text
1
```

It returns the index of the **first occurrence**.

---

# 📌 List Methods — Quick Reference

| Method      | Purpose                          | Example                 |
| ----------- | -------------------------------- | ----------------------- |
| `append()`  | Adds one element at the end      | `list.append(10)`       |
| `extend()`  | Adds multiple elements           | `list.extend([10, 20])` |
| `insert()`  | Adds element at a specific index | `list.insert(1, 10)`    |
| `remove()`  | Removes a value                  | `list.remove(10)`       |
| `pop()`     | Removes element using index      | `list.pop(1)`           |
| `sort()`    | Sorts the list                   | `list.sort()`           |
| `reverse()` | Reverses the list                | `list.reverse()`        |
| `count()`   | Counts occurrences               | `list.count(10)`        |
| `index()`   | Finds first index                | `list.index(10)`        |

---

# 🧠 Important List Concepts

```text
Creating       → []
Indexing       → list[index]
Slicing        → list[start:stop:step]
Adding         → append(), extend(), insert()
Removing       → remove(), pop()
Updating       → list[index] = value
Nested Lists   → [[...], [...]]
Sorting        → sort()
Reversing      → reverse()
Counting       → count()
Finding Index  → index()
```

---

# ⭐ Important Differences

### `append()` vs `extend()`

```python
list1 = [1, 2]

list1.append([3, 4])

# [1, 2, [3, 4]]
```

```python
list1 = [1, 2]

list1.extend([3, 4])

# [1, 2, 3, 4]
```

---

### `remove()` vs `pop()`

```python
list1.remove(20)
```

Removes by **value**.

```python
list1.pop(1)
```

Removes by **index**.

---

### `sort()` vs `reverse()`

```python
list1.sort()
```

Arranges elements in ascending order.

```python
list1.reverse()
```

Reverses the current order.

---

# 📝 Summary

A Python list is an **ordered, mutable collection** that can store multiple values.

The most important operations are:

* **Create** → `[]`
* **Access** → indexing
* **Extract** → slicing
* **Add** → `append()`, `extend()`, `i
