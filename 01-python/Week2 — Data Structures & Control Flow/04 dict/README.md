# 📘 8. Dictionaries in Python

---

## 1. What is a Dictionary?

A **dictionary** is a built-in Python data type that stores data in **key-value pairs**.

- **Key** — identifies the data.
- **Value** — stores the data associated with the key.
- Dictionaries are **mutable**, meaning we can modify them.
- Keys must be unique.
- Dictionaries preserve insertion order.

### Syntax

```python
dictionary = {
    "key1": "value1",
    "key2": "value2"
}
```

### Example

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

print(student)
```

**Output:**

```text
{'name': 'Ashika', 'age': 22, 'mark': 450}
```

---

## 2. Creating a Dictionary

We can create a dictionary using curly braces `{}`.

```python
student = {
    "name": "Ashika",
    "age": 22,
    "course": "Python"
}

print(student)
```

**Output:**

```text
{'name': 'Ashika', 'age': 22, 'course': 'Python'}
```

### Creating an Empty Dictionary

```python
student = {}

print(student)
```

**Output:**

```text
{}
```

---

## 3. Accessing Dictionary Values

We can access values using their keys.

### Using Square Brackets `[]`

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

print(student["name"])
print(student["age"])
```

**Output:**

```text
Ashika
22
```

**Note:** Using a key that does not exist raises a `KeyError`.

### Using the `get()` Method

```python
print(student.get("name"))
print(student.get("city"))
```

**Output:**

```text
Ashika
None
```

The `get()` method returns `None` when the key is missing, unless a default value is provided.

```python
print(student.get("city", "Not Found"))
```

**Output:**

```text
Not Found
```

---

## 4. Adding New Items

Assign a value to a new key to add an item.

```python
student = {
    "name": "Ashika",
    "age": 22
}

student["city"] = "Madurai"

print(student)
```

**Output:**

```text
{'name': 'Ashika', 'age': 22, 'city': 'Madurai'}
```

---

## 5. Updating Existing Values

Assign a new value to an existing key.

```python
student = {
    "name": "Ashika",
    "age": 22
}

student["age"] = 23

print(student)
```

**Output:**

```text
{'name': 'Ashika', 'age': 23}
```

### Using `update()`

```python
student.update({
    "age": 24,
    "city": "Madurai"
})

print(student)
```

The `update()` method adds new keys and updates existing ones.

---

## 6. Removing Items

### `pop()` — Removes a Specific Key

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

student.pop("age")

print(student)
```

**Output:**

```text
{'name': 'Ashika', 'mark': 450}
```

### `popitem()` — Removes the Last Inserted Item

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

student.popitem()

print(student)
```

**Output:**

```text
{'name': 'Ashika', 'age': 22}
```

### `del` — Deletes a Specific Item

```python
del student["age"]

print(student)
```

### `clear()` — Removes All Items

```python
student.clear()

print(student)
```

**Output:**

```text
{}
```

---

## 7. Dictionary Methods

| Method | Purpose |
|---|---|
| `keys()` | Returns all keys |
| `values()` | Returns all values |
| `items()` | Returns key-value pairs |
| `get()` | Safely retrieves a value |
| `update()` | Adds or updates items |
| `pop()` | Removes a specified key |
| `popitem()` | Removes the last inserted item |
| `clear()` | Removes all items |
| `copy()` | Creates a shallow copy |
| `setdefault()` | Returns a value or inserts a default |

### Examples

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

print(student.keys())
print(student.values())
print(student.items())
```

**Output:**

```text
dict_keys(['name', 'age', 'mark'])
dict_values(['Ashika', 22, 450])
dict_items([('name', 'Ashika'), ('age', 22), ('mark', 450)])
```

---

## 8. Looping Through a Dictionary

### Loop Through Keys

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

for key in student:
    print(key)
```

**Output:**

```text
name
age
mark
```

### Loop Through Values

```python
for value in student.values():
    print(value)
```

**Output:**

```text
Ashika
22
450
```

### Loop Through Keys and Values

Use `items()` to access both the key and value.

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

**Output:**

```text
name: Ashika
age: 22
mark: 450
```

---

## 9. Checking Whether a Key Exists

Use the `in` operator to check whether a key exists in a dictionary.

```python
student = {
    "name": "Ashika",
    "age": 22
}

print("name" in student)
print("city" in student)
```

**Output:**

```text
True
False
```

Use `not in` to check whether a key is absent.

```python
print("city" not in student)
```

**Output:**

```text
True
```

**Important:** The `in` operator checks keys by default, not values.

---

## 10. Dictionary Length

Use `len()` to count the number of key-value pairs.

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

print(len(student))
```

**Output:**

```text
3
```

---

## 11. Nested Dictionaries

A dictionary can contain another dictionary as a value.

```python
students = {
    "student1": {
        "name": "Ashika",
        "mark": 450
    },
    "student2": {
        "name": "Roshan",
        "mark": 430
    }
}

print(students["student1"]["name"])
print(students["student2"]["mark"])
```

**Output:**

```text
Ashika
430
```

Nested dictionaries are useful for storing structured information about multiple students, employees, or products.

---

## 12. Dictionary Comprehension

Dictionary comprehension provides a concise way to create dictionaries.

### Syntax

```python
{key: value for item in iterable}
```

### Example

```python
numbers = [1, 2, 3, 4, 5]

squares = {num: num ** 2 for num in numbers}

print(squares)
```

**Output:**

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### With a Condition

```python
numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    num: num ** 2
    for num in numbers
    if num % 2 == 0
}

print(even_squares)
```

**Output:**

```text
{2: 4, 4: 16, 6: 36}
```

---

## 13. Dictionary vs List vs Tuple vs Set

| Feature | Dictionary | List | Tuple | Set |
|---|---|---|---|---|
| Syntax | `{key: value}` | `[]` | `()` | `{}` or `set()` |
| Stores | Key-value pairs | Items | Items | Unique items |
| Mutable | Yes | Yes | No | Yes |
| Allows duplicates | Keys: No | Yes | Yes | No |
| Access | By key | By index | By index | No indexing |

**Note:** An empty `{}` creates a dictionary, not a set. Use `set()` to create an empty set.

---

## 14. Important Rules to Remember

1. Dictionary keys must be unique.
2. If a key is repeated, its latest assigned value is retained.
3. Keys must be hashable, such as strings, integers, or tuples containing only hashable elements.
4. Dictionary values can be of any data type.
5. Dictionaries are mutable.
6. Dictionaries preserve insertion order in modern Python.
7. Use `get()` when a key might not exist.
8. Use `items()` when looping through keys and values.

### Example: Duplicate Keys

```python
data = {
    "name": "Ashika",
    "name": "Nithya"
}

print(data)
```

**Output:**

```text
{'name': 'Nithya'}
```

---

## 15. Real-World Example

### Student Management System

```python
students = {
    "101": {
        "name": "Ashika",
        "age": 22,
        "mark": 450
    },
    "102": {
        "name": "Roshan",
        "age": 22,
        "mark": 430
    },
    "103": {
        "name": "Rahul",
        "age": 23,
        "mark": 420
    }
}

for student_id, details in students.items():
    print(f"ID: {student_id}")
    print(f"Name: {details['name']}")
    print(f"Age: {details['age']}")
    print(f"Mark: {details['mark']}")
    print("-" * 25)
```

This example demonstrates how dictionaries can store and organize structured student records.

---

## 16. Practice Checklist

After studying dictionaries, make sure you can:

- [ ] Create an empty dictionary.
- [ ] Add new key-value pairs.
- [ ] Access values using keys.
- [ ] Update existing values.
- [ ] Remove items using `pop()` and `del`.
- [ ] Use `keys()`, `values()`, and `items()`.
- [ ] Loop through dictionaries.
- [ ] Check whether a key exists.
- [ ] Create nested dictionaries.
- [ ] Use dictionary comprehension.

---

**Next step:** Practice dictionary exercises from Level 1 to Level 5, starting with creating dictionaries and progressing to nested dictionaries and real-world problems.
