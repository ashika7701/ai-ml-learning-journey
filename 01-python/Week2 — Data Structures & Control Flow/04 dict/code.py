# Online Python compiler (interpreter)
# Write and run Python online using this editor.

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

print(student)
```

```python
student = {}

print(student)
```

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

print(student["name"])
print(student["age"])
print(student["mark"])
```

```python
student = {
    "name": "Ashika",
    "age": 22
}

print(student.get("name"))
print(student.get("city", "Not Found"))
```

```python
student = {
    "name": "Ashika",
    "age": 22
}

student["city"] = "Madurai"

print(student)
```

```python
student = {
    "name": "Ashika",
    "age": 22
}

student["age"] = 23

print(student)
```

```python
student = {
    "name": "Ashika",
    "age": 22
}

student.update({
    "age": 23,
    "mark": 450
})

print(student)
```

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

student.pop("age")

print(student)
```

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

student.popitem()

print(student)
```

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

del student["age"]

print(student)
```

```python
student = {
    "name": "Ashika",
    "age": 22
}

student.clear()

print(student)
```

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

print(len(student))
```

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

print(student.keys())
```

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

print(student.values())
```

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

print(student.items())
```

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

for key in student:
    print(key)
```

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

for value in student.values():
    print(value)
```

```python
student = {
    "name": "Ashika",
    "age": 22,
    "mark": 450
}

for key, value in student.items():
    print(f"{key}: {value}")
```

```python
student = {
    "name": "Ashika",
    "age": 22
}

print("name" in student)
print("city" in student)
```

```python
student = {
    "name": "Ashika",
    "age": 22
}

new_student = student.copy()

print(new_student)
```

```python
student = {
    "name": "Ashika",
    "age": 22
}

student.setdefault("city", "Madurai")

print(student)
```

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

```python
numbers = [1, 2, 3, 4, 5]

squares = {
    num: num ** 2
    for num in numbers
}

print(squares)
```

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = {
    num: num ** 2
    for num in numbers
    if num % 2 == 0
}

print(even_numbers)
```

```python
text = "banana"

count = {}

for char in text:
    count[char] = count.get(char, 0) + 1

print(count)
```

```python
students = {
    "Ashika": 450,
    "Roshan": 430,
    "Rahul": 470,
    "Nithya": 420
}

top_student = max(students, key=students.get)

print(top_student)
print(students[top_student])
```

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
    print("-" * 20)
```
