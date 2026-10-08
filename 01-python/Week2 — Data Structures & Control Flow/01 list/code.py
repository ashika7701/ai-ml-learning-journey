#create list in python
listnum=[10,20,30]
print(listnum)

listdup=[10,20,10]
print(listdup)

listmul=[10,20,"ashika"]
print(listmul)

name="ashika"
lists=list(name)
print(lists)

list1=[]
length=int(input("how much value to add into list"))
for i in range(length):
   values=int(input("enter vaule"))
   list1.append(values)
print(list1)


student=[]
length=int(input("enter how much value to add into list"))
for i in range(length):
    values=input("enter value")
    student.append(values)
print(student)


studentna=[]
length=int(input("enter how much value to add into list"))
for i in range(length):
    value=input("Enter vaules for list")
    if value.isdigit():
        value=int(value)
    studentna.append(value)
print(studentna)
