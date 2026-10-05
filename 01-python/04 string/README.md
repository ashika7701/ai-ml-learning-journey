# 🐍 Python Strings

A **string** is a sequence of characters enclosed inside **single quotes (`' '`), double quotes (`" "`), or triple quotes (`''' '''` / `""" """`)**.

```python
name = "Python"
language = 'Python'
message = """Python is easy to learn."""
```

---

# 1. 📌 String Indexing

**Indexing** is used to access individual characters from a string.

Python uses **zero-based indexing**, which means the first character has index `0`.

### Example

```python
text = "Python"

print(text[0])
print(text[1])
print(text[5])
```

**Output:**

```text
P
y
n
```

### Positive Indexing

```text
String:    P   y   t   h   o   n
Index:     0   1   2   3   4   5
```

### Negative Indexing

Python also supports **negative indexing**, which starts from the end.

```text
String:     P    y    t    h    o    n
Negative:  -6   -5   -4   -3   -2   -1
```

### Example

```python
text = "Python"

print(text[-1])
print(text[-2])
print(text[-6])
```

**Output:**

```text
n
o
P
```

> 💡 **Remember:** `0` → first character, `-1` → last character.

---

# 2. ✂️ String Slicing

**Slicing** is used to extract a portion of a string.

### Syntax

```python
string[start:stop]
```

* `start` → starting index **included**
* `stop` → ending index **excluded**

### Example

```python
text = "Python"

print(text[0:3])
```

**Output:**

```text
Pyt
```

The characters at indexes `0`, `1`, and `2` are selected.

### Slicing Diagram

```text
String:    P   y   t   h   o   n
Index:     0   1   2   3   4   5

text[1:4]
           ↑       ↑
         start    stop

Result: "yth"
```

---

## 2.1 Omitting Start

If `start` is omitted, Python starts from the beginning.

```python
text = "Python"

print(text[:4])
```

**Output:**

```text
Pyth
```

---

## 2.2 Omitting Stop

If `stop` is omitted, Python continues until the end.

```python
text = "Python"

print(text[2:])
```

**Output:**

```text
thon
```

---

## 2.3 Negative Slicing

```python
text = "Python"

print(text[-4:-1])
```

**Output:**

```text
tho
```

---

## 2.4 Step in Slicing

### Syntax

```python
string[start:stop:step]
```

Example:

```python
text = "Python"

print(text[0:6:2])
```

**Output:**

```text
Pto
```

Indexes `0`, `2`, and `4` are selected.

---

## 2.5 Reverse a String

A common slicing technique is:

```python
text = "Python"

print(text[::-1])
```

**Output:**

```text
nohtyP
```

> 💡 `[::-1]` means **start → end → move backward by 1**.

---

# 3. 🛠️ String Methods

String methods are **built-in methods used to perform operations on strings**.

Some commonly used string methods are:

| Method         | Purpose                             |
| -------------- | ----------------------------------- |
| `upper()`      | Converts to uppercase               |
| `lower()`      | Converts to lowercase               |
| `strip()`      | Removes leading/trailing whitespace |
| `replace()`    | Replaces text                       |
| `split()`      | Splits a string into a list         |
| `join()`       | Combines strings                    |
| `find()`       | Finds the index of text             |
| `startswith()` | Checks the beginning                |
| `endswith()`   | Checks the ending                   |

> ⚠️ Strings are **immutable** in Python. String methods generally return a **new string** instead of changing the original string.

---

# 4. 🔠 `upper()`

The `upper()` method converts all alphabetic characters in a string to **uppercase**.

### Syntax

```python
string.upper()
```

### Example

```python
text = "hello python"

result = text.upper()

print(result)
```

**Output:**

```text
HELLO PYTHON
```

### Important

```python
text = "python"

text.upper()

print(text)
```

**Output:**

```text
python
```

The original string is unchanged because strings are immutable.

To store the result:

```python
text = text.upper()

print(text)
```

**Output:**

```text
PYTHON
```

---

# 5. 🔡 `lower()`

The `lower()` method converts all alphabetic characters in a string to **lowercase**.

### Syntax

```python
string.lower()
```

### Example

```python
text = "HELLO PYTHON"

print(text.lower())
```

**Output:**

```text
hello python
```

### Practical Example

```python
username = "ADMIN"

if username.lower() == "admin":
    print("Valid username")
```

**Output:**

```text
Valid username
```

---

# 6. 🧹 `strip()`

The `strip()` method removes **leading and trailing whitespace** from a string.

### Syntax

```python
string.strip()
```

### Example

```python
text = "   Python   "

print(text.strip())
```

**Output:**

```text
Python
```

It removes spaces from the **beginning and end**, but not from the middle.

```python
text = "   Python Programming   "

print(text.strip())
```

**Output:**

```text
Python Programming
```

### Related Methods

#### `lstrip()`

Removes whitespace from the **left side**.

```python
text = "   Python"

print(text.lstrip())
```

#### `rstrip()`

Removes whitespace from the **right side**.

```python
text = "Python   "

print(text.rstrip())
```

---

# 7. 🔄 `replace()`

The `replace()` method is used to **replace one part of a string with another**.

### Syntax

```python
string.replace(old, new)
```

### Example

```python
text = "I like Java"

result = text.replace("Java", "Python")

print(result)
```

**Output:**

```text
I like Python
```

### Replacing Multiple Occurrences

```python
text = "apple apple apple"

print(text.replace("apple", "mango"))
```

**Output:**

```text
mango mango mango
```

### Using `count`

You can specify how many replacements should happen.

```python
text = "apple apple apple"

print(text.replace("apple", "mango", 2))
```

**Output:**

```text
mango mango apple
```

---

# 8. ✂️ `split()`

The `split()` method divides a string into **multiple parts** and returns them as a **list**.

### Syntax

```python
string.split(separator)
```

### Example

```python
text = "Python is easy"

words = text.split()

print(words)
```

**Output:**

```text
['Python', 'is', 'easy']
```

By default, `split()` uses whitespace as the separator.

### Using a Separator

```python
text = "Python,Java,C++"

languages = text.split(",")

print(languages)
```

**Output:**

```text
['Python', 'Java', 'C++']
```

### Practical Example

```python
name = "John David Smith"

parts = name.split()

print(parts)
```

**Output:**

```text
['John', 'David', 'Smith']
```

> 💡 `split()` → **String → List**

---

# 9. 🔗 `join()`

The `join()` method is used to **combine multiple strings into a single string** using a separator.

### Syntax

```python
separator.join(iterable)
```

### Example

```python
words = ["Python", "is", "easy"]

result = " ".join(words)

print(result)
```

**Output:**

```text
Python is easy
```

### Using a Comma

```python
languages = ["Python", "Java", "C++"]

result = ", ".join(languages)

print(result)
```

**Output:**

```text
Python, Java, C++
```

### Using a Hyphen

```python
letters = ["P", "y", "t", "h", "o", "n"]

print("-".join(letters))
```

**Output:**

```text
P-y-t-h-o-n
```

> 💡 `join()` → **List/iterable → String**

### `split()` vs `join()`

```text
split()  → String → List
join()   → List → String
```

---

# 10. 🔍 `find()`

The `find()` method searches for a substring and returns its **first index**.

### Syntax

```python
string.find(substring)
```

### Example

```python
text = "Python Programming"

result = text.find("Programming")

print(result)
```

**Output:**

```text
7
```

### If the Text Is Not Found

```python
text = "Python"

print(text.find("Java"))
```

**Output:**

```text
-1
```

> 💡 `find()` returns **`-1`** when the substring is not found.

### Example

```python
text = "Hello World"

print(text.find("World"))
```

**Output:**

```text
6
```

---

# 11. 🚀 `startswith()`

The `startswith()` method checks whether a string **starts with a specified substring**.

It returns either `True` or `False`.

### Syntax

```python
string.startswith(prefix)
```

### Example

```python
text = "Python Programming"

print(text.startswith("Python"))
```

**Output:**

```text
True
```

### Example

```python
text = "Python Programming"

print(text.startswith("Java"))
```

**Output:**

```text
False
```

### Practical Example

```python
filename = "data.csv"

print(filename.startswith("data"))
```

**Output:**

```text
True
```

---

# 12. 🏁 `endswith()`

The `endswith()` method checks whether a string **ends with a specified substring**.

It returns either `True` or `False`.

### Syntax

```python
string.endswith(suffix)
```

### Example

```python
text = "Python Programming"

print(text.endswith("Programming"))
```

**Output:**

```text
True
```

### Example

```python
text = "Python Programming"

print(text.endswith("Python"))
```

**Output:**

```text
False
```

### Practical Example

```python
filename = "data.csv"

print(filename.endswith(".csv"))
```

**Output:**

```text
True
```

---

# 📚 String Methods — Quick Reference

| Method         | Description                         | Example                            |
| -------------- | ----------------------------------- | ---------------------------------- |
| `upper()`      | Converts to uppercase               | `"python".upper()`                 |
| `lower()`      | Converts to lowercase               | `"PYTHON".lower()`                 |
| `strip()`      | Removes leading/trailing whitespace | `" Python ".strip()`               |
| `replace()`    | Replaces text                       | `"Java".replace("Java", "Python")` |
| `split()`      | Converts string into a list         | `"A B C".split()`                  |
| `join()`       | Combines strings                    | `" ".join(["A", "B"])`             |
| `find()`       | Finds substring index               | `"Python".find("th")`              |
| `startswith()` | Checks starting text                | `"Python".startswith("Py")`        |
| `endswith()`   | Checks ending text                  | `"Python".endswith("on")`          |

---

# 🧠 Important Concepts to Remember

### 1. Indexing

```python
text = "Python"

print(text[0])     # P
print(text[-1])    # n
```

**Indexing → Access one character**

---

### 2. Slicing

```python
text = "Python"

print(text[1:4])
```

**Output:**

```text
yth
```

**Slicing → Extract a portion of a string**

---

### 3. `split()` and `join()`

```python
text = "Python is easy"

words = text.split()

result = "-".join(words)

print(result)
```

**Output:**

```text
Python-is-easy
```

**Remember:**

```text
split() → String → List
join()  → List → String
```

---

### 4. Search and Check Methods

```python
text = "Python Programming"

print(text.find("Python"))
print(text.startswith("Python"))
print(text.endswith("Programming"))
```

**Output:**

```text
0
True
True
```

---

# 🎯 Summary

```text
String
│
├── Indexing
│   ├── Positive indexing
│   └── Negative indexing
│
├── Slicing
│   ├── [start:stop]
│   ├── [start:]
│   ├── [:stop]
│   └── [start:stop:step]
│
└── String Methods
    ├── upper()       → Uppercase
    ├── lower()       → Lowercase
    ├── strip()       → Remove surrounding whitespace
    ├── replace()     → Replace text
    ├── split()       → String → List
    ├── join()        → List → String
    ├── find()        → Find index
    ├── startswith()  → Check beginning
    └── endswith()    → Check ending
```

> ⭐ **Key Point:** Python strings are **ordered, indexed, immutable sequences of characters**.
