# Online Python compiler (interpreter)
# Write and run Python online using this editor.
num=(10,)#tuple
num2=(10)#int
num1=1,23,3
print(type(num1))
print(type(num2))
print(type(num))

numbers = (10, 20, 30, 40, 50)
#positive indexing
print(numbers[0])
print(numbers[2])
print(numbers[4])
#negative indexing
print(numbers[-1])
print(numbers[-2])
print(numbers[-5])

#slicing
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
#step indexing


print(numbers[::2])
print(numbers[1::2])
print(numbers[::-1])
student=("ashika",10,10)
print(student)
print(student[1])
print(student[2])
print(student[1:2])
ni,n1,gt=student
print(ni)
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
numbers = (10, 20, 30, 40)

print(20 in numbers)
print(50 not in numbers)

print(numbers.index(30))
