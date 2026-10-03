# Online Python compiler (interpreter)
# Write and run Python online using this editor.
#data types in python
name="ashika"
print("name:",name)
print(type(name))
age=22
print("your age is ",age)
print(type(age))
weight=54.56
print("your weight is", weight)
print(type(weight))
num1=int(30.5)
print(num1)
num2=float(10)
print(num2)
num1=int("20")
print(num1)
print(num2+num1)#int+float=float
phone_no=86680253456

#python has automatically store he large number but in other language have long int 
h=12.3e4
v=12.3e-4
print(h)
print(v)

#string operation
name="Roshan ashika"
print(name[1])
print(name[2])
print(name[4:6])
print(name[-2])
print(name[-1:-3])
print(name.upper())
print(name.lower())
print(name.split())
print(len(name))
first_name="Karthick"
last_name=" roshan "
full_name=first_name + " " +last_name
print(full_name)
print(full_name.strip())
print(full_name.replace("roshan","ashika"))
message = f"My name is {name} and I am {age} years old."
print(message)
# complex
x=3+4j
y=4+9j
print(x+y)

print(x.imag)
print(x.real)
z=complex(5,6)
print(z)

is_student=True
is_teacher=True
print(is_student)
print(is_teacher)
print(type(is_student))
age = 20

print(age > 18)
print(age < 18)
print(age == 20)
age = 20

if age >= 18:
    print("Eligible")
print(bool(1))
print(bool(""))
print(bool("ashika"))
x="ashika"
print(bool(x))
age = 25
has_id = True
print(age >= 18 and has_id)
x1=""
print(x1)
name=None
if name is None:
  print("NAME IS NO PROVIDE")

name="ashika"
if name is not None:
  print("name is provided")


