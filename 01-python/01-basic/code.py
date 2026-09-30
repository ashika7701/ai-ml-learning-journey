#first program
print("hello world")

# comments in python
#this is the single line comment
#this 
#is
#multi 
#line 
#comment

"""doc string is used to documentation but mostly python python doesn't have the 
multline string"""

#indentation is space used to control the program
age =25
if age>18:
  print("you are major")
else:
  print("you are not major")

for i in range(1,5,1):
  print(i)

def add():
  a=10
  b=20
  print(a+b)
add()

#variables
a=10
print(a)
name="ashika"
print("Name", name)
age=22
print("age", age)

#variable name rules
user_name="ashika"
#user-name wrong
user_name1="roshan"
#1user_name="roshan" wrong

#$user_name wrong

#name conversion
Age=25
print(age)
#we should be print Age

#multi-assignment
name,age,roll_no="priya",35,1003
#f-string
print(f"my name is {name} my age is {age} roll no. is{roll_no}")
#without f-string
print("my name is", name "my age is", age "roll no is", roll_no)

#change variable
height=154
height=170
print("height", height)

#object and variable whethere the object this refer to the another variable

x=10
y=x
print(x is y)

#inputs and output
z="hello"
print(z,"everyone")
#integer
a=10
print("number",a)
a1=int(input("enter the number"))
print(a1)
#string
b="ashika"
print("my name is",b)
b1=input("enter your name")
print("your name is ", b1)
#float
c=1.2
print("float vaule", c)
c1=float(input("enter the float vaule"))
print("the float vaule is", c1)



